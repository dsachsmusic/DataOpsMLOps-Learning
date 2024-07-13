- Create a free Snowflake trial account 
- Create a free Hubspot trial account
- Download and import dummy data from https://community.hubspot.com/t5/Share-Your-Work/How-to-create-Hubspot-test-dummy-data/-  m-p/547034 into Hubspot
- In Snowflakem go to Partner Connect, and select Stitch - allow it to create the free trial/connect to your account. Set up - the integration with the Snowflake Data Warehouse.
- In Stitch.... Integrations >  Add Integration > Hubspot ... set up integration (connecting Hubspot to Snowflake)/extract data - into Snowflake
- In Snowflake > Data Products > Marketplace...select U.S. Zip Code Metadata (Free) > Get...follow any setps ....to set up the - database 
- In Snowflake > Data > Databases
  - Confirm you see PC_STITCH_DB, and, within it, a schema with a name matching the Hubspot integration
  - COnfirm you see U_S_ZIP_CODE_METADATA
- In Snowflake > Projects > Worksheets > click "+" > SQL Worksheet to create a new worksheet
- Run the following:
```
-- set the Role
USE ROLE accountadmin; -- default that comes with the Snowflake trial

-- set the Warehouse
USE WAREHOUSE compute_wh; -- default that comes with the Snowflake trial

-- create a new database, and schema to hold a new table we'll create via joins
CREATE DATABASE HUBSPOT_SNOWFLAKE_LOADED;

CREATE SCHEMA HUBSPOT_SNOWFLAKE_LOADED.misc


-- Create a new table. 
CREATE TABLE HUBSPOT_SNOWFLAKE_LOADED.misc.tbl_aggregate_latitudelines_revenue (
    latitudeline VARCHAR(50),
    company_names ARRAY,
    latitudeline_states ARRAY,
    total_revenue FLOAT
);

/*
Run an insert to populate the table...
The resulting table shows the aggregate total revenue of companies (the company records in Hubspot account) by latitude line......
Note: when we extract the data using the Stitch integration, the resulting table is made up of cells with JSON objects...
in them.  In particular, one column, "Properties" has, for each row, a JSON object with all the properties for that given...
record.  We can select out  values from that JSON object within the select statement(via parsing, and assigning them a type)...
using syntax like COLUMNNAME:key::STRING, or (COLUMNNAME:key.key::STRING)
*/
INSERT INTO HUBSPOT_SNOWFLAKE_LOADED.misc.tbl_aggregate_latitudelines_revenue  (latitudeline, company_names, latitudeline_states, total_revenue)
SELECT 
    SUBSTRING(zd.latitude, 1, CHARINDEX('.', zd.latitude) - 1) AS latitudeline, trim off decimal point and subsequent values, making latitude line a whole number
    ARRAY_AGG(ish.PROPERTIES:name.value::STRING) AS company_names, -- array of companies for the given group created using GROUP BY
    ARRAY_AGG(DISTINCT zd.state) AS latitudeline_states, -- array of states for the given group created using GROUP BY
    SUM(CAST(ish.PROPERTIES:annualrevenue.value::STRING AS FLOAT)) AS total_revenue
FROM 
    PC_STITCH_DB.INTEGRATION_STITCH_HUBSPOT.COMPANIES AS ish
INNER JOIN 
    /* joins Hubspot company data to zip code data from marketplace ...which has latitude lines as a value*/
	U_S__ZIP_CODE_METADATA.ZIP_DEMOGRAPHICS.ZIP_CODE_METADATA AS zd 
ON 
    ish.PROPERTIES:zip.value::STRING = zd.zip
WHERE
    ish.PROPERTIES:annualrevenue.value::STRING IS NOT NULL
GROUP BY 
    latitudeline
ORDER BY 
    latitudeline DESC;
```

In Snowflake > Projects > Dashboards...click "+ Dashboard"...name the Dashboard "Visualize-hubspot-test"
...and, "New Tile" > "From SQL Worksheet"...and, add the following query:
```
/*this query selects the all values except the greatest value...
because, given the Hubspot data we have, the total revenue value that corresponds to ...
the latitude line 42, incidentally, is orders of magnitude greater than the others...
and, this is a simple way I used to get the visualization to look like something useful...
...there is probably a way to do this better, that doesn't exclude a column
*/
SELECT * FROM
    HUBSPOT_SNOWFLAKE_LOADED.MISC.TBL_AGGREGATE_LATITUDELINES_REVENUE
WHERE 
	total_revenue NOT IN (
		SELECT MAX(total_revenue)
		FROM HUBSPOT_SNOWFLAKE_LOADED.MISC.TBL_AGGREGATE_LATITUDELINES_REVENUE
	);
```

Next steps
- Consider doing the same ETL in Python (Snowflake > Projects > Worksheets > click "+" > SQL Worksheet)
- Schedule the transform SQL query (the one that inserts into tbl_aggregate_latitudelines_revenue), so that it updates as Hubspot updates
  - Create a stored procedure that deletes values from the table, and then (re) performs the insert
  - Create a Snowflake Task, via the syntax CREATE OR REPLACE TASK...
  - Ideally, schedule it to happen only if there is a change
- Enable dashboarding using Tableau, or similar 
  - This would require a csv...
    - Making it manually would mean it does not automatically update...
	  - Could do it via an AWS Lamda, however, this involves setting up  an AWS S3 bucket as a "stage" in Snowflake
	    - ...and there are obstacles...clear text secrets vs challenge using IAM with the Snowflake trial

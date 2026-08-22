---
title: "Example: Connecting to Google Cloud BigQuery via a JSON Connection"
id: 28897883304077
section: "Connecting to Your Data Sources - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897883304077-Example-Connecting-to-Google-Cloud-BigQuery-via-a-JSON-Connection
updated_at: 2024-09-30T09:12:56Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Example: Connecting to Google Cloud BigQuery via a JSON Connection

This topic presents an example about how you can set up a JSON connection in a catalog to use the JSON data on Google Cloud BigQuery.

In this example, we use two parameters to provide values for the two tokens, access_token and maxResults, in the URL of the JSON instance file on Google Cloud BigQuery. access_token is for authorizing a Google API request and maxResults represents the maximum record number to return. You can change the parameter values to submit dynamic tokens at runtime.

- Make sure SampleReports.cat is the currently open catalog file. If not, navigate to File > Open Catalog to open it from <install_root>\Demo\Reports\SampleReports.

- Right-click the Parameters node in Data Source 1 of the catalog and select New Parameter from the shortcut menu.

- In the New Parameter dialog box, type pAccessToken in the Name text box.

- Select String from the Value Type drop-down list.

- Select Add to add a value line, then double-click in the line and type the valid token value to access Google Cloud BigQuery, for example, ya29.Ci9dA2sA8J_wM8e5FnY9rJg551153GQWGbleO-y9aeZOky9V36Tz497HY1chApjLFg.

- Select OK to create the parameter.  

- Repeat the preceding steps to create another parameter pMaxResults of Integer type with the prompt value 2.
    

- Right-click the Data Source 1 node and select New JSON Connection from the shortcut menu.

- In the Extract JSON Schema screen of the JSON Connection Wizard dialog box, select Extract Schema from Instance Data from the Schema Source drop-down list.

- Type the following URL in the Instance text box:
 https://www.googleapis.com/bigquery/v2/projects/bigquery-public-data/datasets/samples/tables/gsod/data?maxResults=@pMaxResults&access_token=@pAccessToken.

- Select Next until Designer displays the Add Table screen.

- Select f in the Tables box and select Add to add it to the Added Tables box.

- Select Finish to set up the connection.

Previous Topic  Next Topic

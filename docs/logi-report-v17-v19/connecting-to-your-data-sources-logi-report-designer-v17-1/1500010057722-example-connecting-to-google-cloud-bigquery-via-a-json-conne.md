---
title: "Example: Connecting to Google Cloud BigQuery via a JSON Connection"
id: 1500010057722
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057722-Example-Connecting-to-Google-Cloud-BigQuery-via-a-JSON-Connection
updated_at: 2021-07-23T19:14:56Z
---

# Example: Connecting to Google Cloud BigQuery via a JSON Connection

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057762-Working-with-JSON-Connections-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057882-Connecting-via-XML-Connections)

# Example: Connecting to Google Cloud BigQuery via a JSON Connection

This topic presents an example about how you can set up a JSON connection to connect a catalog to Google Cloud BigQuery.

In this example, we create two parameters in the catalog and use them to provide values for the two tokens access\_token and maxResults in the URL of the JSON instance file used to access Google Cloud BigQuery. The token access\_token is for authorizing a Google API request, and maxResults represents the maximum record number to return. You can change the parameter values to provide dynamic values for the two tokens at runtime.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Right-click the **Parameters** node in Data Source 1 of the catalog and select **New Parameter** from the shortcut menu.
3. In the New Parameter dialog box, type **pAccessToken** in the **Name** text box.
4. Select **String** from the **Value Type** drop-down list.
5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a value line, double-click in it and then type in the valid token value to access Google Cloud BigQuery, for example, ya29.Ci9dA2sA8J\_wM8e5FnY9rJg551153GQWGbleO-y9aeZOky9V36Tz497HY1chApjLFg.
6. Select **OK** to create the parameter.

   ![New Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857019927/cnctn_json_stup1.gif)
7. Repeat the above steps to create another parameter **pMaxResults** of Integer type with the prompt value **2** in the Value List.

   ![New Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857020183/cnctn_json_stup2.gif)

   For more information about creating parameters, see [Creating a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog).
8. Right-click the **Data Source 1** node and select **New JSON Connection** from the shortcut menu. Designer displays the JSON Connection Wizard.
9. In the **Extract JSON Schema** screen, select **Extract Schema from Instance Data** from the **Schema Source** drop-down list.
10. Type the following URL in the **Instance** text box:

    `https://www.googleapis.com/bigquery/v2/projects/bigquery-public-data/datasets/samples/tables/gsod/data?maxResults=@pMaxResults&access_token=@pAccessToken`

    ![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/4404848651927/cnctn_json_stup3.gif)
11. Select **Next** three times to go to the **Add Table** screen. Select **f** in the **Tables** box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the **Added Tables** box.
12. Select **Finish** to set up the connection.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057762-Working-with-JSON-Connections-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057882-Connecting-via-XML-Connections)

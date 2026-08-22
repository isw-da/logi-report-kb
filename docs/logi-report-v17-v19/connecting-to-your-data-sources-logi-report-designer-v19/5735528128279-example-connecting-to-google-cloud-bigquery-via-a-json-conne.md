---
title: "Example: Connecting to Google Cloud BigQuery via a JSON Connection"
id: 5735528128279
section: "Connecting to Your Data Sources - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735528128279-Example-Connecting-to-Google-Cloud-BigQuery-via-a-JSON-Connection
updated_at: 2022-11-02T04:29:03Z
---

# Example: Connecting to Google Cloud BigQuery via a JSON Connection

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521660439-Accessing-Data-via-XML-Connections)

# Example: Connecting to Google Cloud BigQuery via a JSON Connection

This topic presents an example about how you can set up a JSON connection in a catalog to use the JSON data on Google Cloud BigQuery.

In this example, we use two parameters to provide values for the two tokens, access\_token and maxResults, in the URL of the JSON instance file on Google Cloud BigQuery. access\_token is for authorizing a Google API request and maxResults represents the maximum record number to return. You can change the parameter values to submit dynamic tokens at runtime.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Right-click the **Parameters** node in Data Source 1 of the catalog and select **New Parameter** from the shortcut menu.
3. In the New Parameter dialog box, type **pAccessToken** in the **Name** text box.
4. Select **String** from the **Value Type** drop-down list.
5. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a value line, then double-click in the line and type the valid token value to access Google Cloud BigQuery, for example, **ya29.Ci9dA2sA8J\_wM8e5FnY9rJg551153GQWGbleO-y9aeZOky9V36Tz497HY1chApjLFg**.
6. Select **OK** to [create the parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735516481047-Creating-Parameters-in-a-Catalog).

   ![New Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898533758359/cnctn_json_stup1.gif)
7. Repeat the preceding steps to create another parameter **pMaxResults** of Integer type with the prompt value **2**.

   ![New Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898533764247/cnctn_json_stup2.gif)
8. Right-click the **Data Source 1** node and select **New JSON Connection** from the shortcut menu.
9. In the **Extract JSON Schema** screen of the JSON Connection Wizard dialog box, select **Extract Schema from Instance Data** from the **Schema Source** drop-down list.
10. Type the following URL in the **Instance** text box:
    `https://www.googleapis.com/bigquery/v2/projects/bigquery-public-data/datasets/samples/tables/gsod/data?maxResults=@pMaxResults&access_token=@pAccessToken`.

    ![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/9898533768087/cnctn_json_stup3.gif)
11. Select **Next** until Designer displays the **Add Table** screen.
12. Select **f** in the **Tables** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add it to the **Added Tables** box.
13. Select **Finish** to set up the connection.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521660439-Accessing-Data-via-XML-Connections)

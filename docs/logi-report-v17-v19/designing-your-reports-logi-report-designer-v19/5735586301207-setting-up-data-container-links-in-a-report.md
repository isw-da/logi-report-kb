---
title: "Setting Up Data Container Links in a Report"
id: 5735586301207
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735586301207-Setting-Up-Data-Container-Links-in-a-Report
updated_at: 2022-11-02T08:18:58Z
---

# Setting Up Data Container Links in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report)

# Setting Up Data Container Links in a Report

In a page or ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")web report, when two [data containers](https://devnet.logianalytics.com/hc/en-us/articles/5735520464535-Working-with-Components-in-Reports#DC) in a parent-child relationship apply different datasets, you can use a data container link to set up data relation between them. This topic introduces data container links and provides examples describing how you can apply them in a report.

This topic contains the following sections:

* [What Is a Data Container Link?](#What)
* [Example: Adding a Data Container Link in a Report](#Example)

## What Is a Data Container Link?

A data container includes:

* A set of link conditions that dynamically filters data in child data containers.
* A set of parameter links that assign fixed values to parameters of both data containers, so users do not need to specify values for the parameters at runtime. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")However, you cannot return values to parameters of the parent data container when setting up a data container link in web reports.

Generally, a data container link functions the same as a [subreport](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports) link. The only difference is that you do not need to specify the child component in a data container link, because you have already selected the child data container as the target of the link at the very beginning.

## Example: Adding a Data Container Link in a Report

Assume that you have a [banded object](https://devnet.logianalytics.com/hc/en-us/articles/5735511901079-Inserting-Banded-Objects-in-a-Report) showing the customer information, then you [insert a table](https://devnet.logianalytics.com/hc/en-us/articles/5735521199255-Inserting-Tables-in-a-Report) into the detail panel of the banded object using another dataset, which displays the order information. Now you want to set up a data link between the banded object and the table, so that when you view the report, you can get a table according to the customer ID.

![Data Container Link Example](https://devnet.logianalytics.com/hc/article_attachments/9898457649815/rpt_cntnrlnk1.gif)

You can achieve this by taking the steps:

1. Select the table and right-click it.
2. On the shortcut menu, select **Data Container Link**. Designer displays the [Link Data Container dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523785367-Link-Data-Container-Dialog-Box).
3. In the **Condition** tab, select the **Customer ID** field from the dataset of the banded object in the left box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif).
4. In the **Field** box, Designer applies the "=" operator by default and automatically selects **Customer ID** from the drop-down list in the **Fields (Child)** column, because it figures out that the dataset the table applies contains the same field. A link condition based on the Customer ID field is now created between the two data containers.

   ![Set Link Condition Based on Customer ID](https://devnet.logianalytics.com/hc/article_attachments/9898474728983/rpt_cntnrlnk2.gif)
5. Select **OK** to apply the link.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report)

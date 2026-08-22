---
title: "Setting Up Data Container Links in a Report"
id: 45190670675085
section: "Designing Your Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190670675085-Setting-Up-Data-Container-Links-in-a-Report
updated_at: 2026-04-30T15:16:04Z
source_host: logi-report-v26.insightsoftware.com
---
# Setting Up Data Container Links in a Report

In a page or web report, when two data containers in a parent-child relationship  apply different datasets, you can use a data container link to set up data relation between them. This topic introduces data container links and provides examples describing how you can apply them in a report.

This topic contains the following sections:

- What Is a Data Container Link?

- Example: Adding a Data Container Link in a Report

## 
What Is a Data Container Link?
            

A data container includes:

- A set of link conditions that dynamically filters data in child data containers.

- A set of parameter links that assign fixed values to parameters of both data containers, so users do not need to specify values for the parameters at runtime. However, you cannot  return values to parameters of the parent data container when setting up a data container link in web reports.

Generally, a data container link functions the same as a subreport link. The only difference is that you do not need to specify the child component in a data container link, because you have already selected the child data container as the target of the link at the very beginning. 

## 
Example: Adding a Data Container Link in a Report

Assume that you have a banded object showing the customer information, then you insert a table into the detail panel of the banded object using another dataset, which displays the order information. Now you want to set up a data link between the banded object and the table, so that when you view the report, you can get a table according to the customer ID.

You can achieve this by taking the steps:

- Select the table and right-click it.

- On the shortcut menu, select Data Container Link. Designer displays the Link Data Container dialog box.
			  

- In the Condition tab, select the Customer ID field from the dataset of the banded object  in the left box and select Add.

-  In the Field box, Designer applies the "=" operator by default and automatically selects Customer ID from the drop-down list in the Fields (Child) column, because it figures out that the dataset the table applies contains the same field. A link condition based on the Customer ID field is now created between the two data containers.
				

- Select OK to apply the link.

---
title: "Logi Report v19.1 Enhancements"
id: 7985355826455
section: "Release Notes for Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/7985355826455-Logi-Report-v19-1-Enhancements
updated_at: 2022-10-31T17:18:50Z
---

# Logi Report v19.1 Enhancements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985329729687-Logi-Report-v19-1-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741437478167-Logi-Report-v19-Release-Notes)

# Logi Report v19.1 Enhancements

This topic introduces the significant features of Logi Report v19.1.

* [Improved Report UX](#ReportUI)
* [Enhanced Embedding Capabilities](#Embedding)

## Improved Report UX

* You can now bookmark web reports and manage bookmarks at the report level in Web Report Studio.

  ![Bookmark Web Reports and Manage Bookmarks](https://devnet.logianalytics.com/hc/article_attachments/9905612854551/bookmark.png)
* You can now apply different formatting to the title and entries of each level in the table of contents of your reports.

  ![Format TOC Title & Levels](https://devnet.logianalytics.com/hc/article_attachments/9905612887063/format-toc-title-level.jpg)
* You can now use the Maximum Length property on the Chart Paper object to specify the maximum number of characters you want to display in the category names, when you specify to truncate the names.

  ![Maximum Chart Category Name Length](https://devnet.logianalytics.com/hc/article_attachments/9905612920727/max-chart-category-length.jpg)
* You can now use crosstab formulas in web reports and business view-based page reports, in addition to query-based page reports. You can also create and edit crosstab formulas in Web/Page Report Studio at runtime, add them in crosstabs as aggregations, and use them to control property values and perform conditional formatting of crosstab fields.

  ![Create and Edit Crosstab Formula](https://devnet.logianalytics.com/hc/article_attachments/9905612954391/crosstab-formula.png)
* You can now define dynamic bursting file names to include field values when scheduling report bursting tasks, by using "recipMapping\_<colName>" in file names.

  ![Define Dynamic Bursting File Name](https://devnet.logianalytics.com/hc/article_attachments/9905575010071/dynamic-file-name.png)
* When creating links on data markers in charts in both Designer and Web Report Studio, you can now use Current Category/Series in the link conditions, URLs, or email addresses, to enable users to generate dynamic links from different chart categories/series.

  ![Dynamically Define Chart Links Using Current Category/Series](https://devnet.logianalytics.com/hc/article_attachments/9905575054871/current-category.png)

## Enhanced Embedding Capabilities

* You can now customize all common and specific properties for Web Report Studio, Page Report Studio, and JDashboard together in the server profile at the task level more conveniently, using either the Server Console or API.

  ![Customize Profile for Web Report Studio, Page Report Studio, and JDashboard Together](https://devnet.logianalytics.com/hc/article_attachments/9905613053719/customize-profile.png)
* In Web/Page Report Studio, data components in one report can now share and inherit datasets and dataset filters for better performance, and you can manage datasets as you do in Designer.

  ![Dataset Share and Management](https://devnet.logianalytics.com/hc/article_attachments/9905613071127/share-dataset-in-studio.png)
* You can now get, create, update, and delete organizations, as well as get and update the resource allocation of organizations, using the JavaScript REST API.

  ![Manage Organizations Using the JavaScript REST API](https://devnet.logianalytics.com/hc/article_attachments/9905575135767/organization-api.png)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985329729687-Logi-Report-v19-1-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741437478167-Logi-Report-v19-Release-Notes)

---
title: "Logi Report v19.2 Enhancements"
id: 9905923636759
section: "Release Notes for Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9905923636759-Logi-Report-v19-2-Enhancements
updated_at: 2022-11-07T02:50:39Z
---

# Logi Report v19.2 Enhancements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9905923590551-Logi-Report-v19-2-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/7985329729687-Logi-Report-v19-1-Release-Notes)

# Logi Report v19.2 Enhancements

This topic introduces the significant features of Logi Report v19.2.

* [Self-Service Usability](#Self)
* [User Experience Improvements](#UX)
* [Embedding Capability Enhancements](#Embed)

## Self-Service Usability

Server now provides a template editor called Logi Report Studio. You can use this to edit page report templates. You can create and update tables, banded objects, and crosstabs by dragging data fields directly, as well as updating object properties via the Inspector panel.

![Logi Report Studio](https://devnet.logianalytics.com/hc/article_attachments/9905902914583/lrstudio.png)

## User Experience Improvements

* You can now customize the page layout of your report for different outputs to display the outputs either in multiple pages or a single page, using Designer and Web/Page Report Studio.

  ![Customize Report Page Layout](https://devnet.logianalytics.com/hc/article_attachments/9905902969495/page-layout.png)
* You can now insert text boxes in web reports and business view-based page reports, using Designer. Server now displays text boxes in Web Report Studio as it does in Page Report Studio.

  ![Use Text Box in Web Report](https://devnet.logianalytics.com/hc/article_attachments/9905931369751/text-box.jpg)
* You can now use the new built-in functions, *currentGroup()*, *currentGroupLevel()*, *getAllGroups()*, *getAllSortColumns()*, *getGroupBy()*, and *getSortBy()*, to get the group-by and sort-by columns of tables and banded objects in your reports, using both Designer and Web Report Studio.

  ![New Formula Functions to Get Group and Sort Columns](https://devnet.logianalytics.com/hc/article_attachments/9905903028759/formula-function.jpg)
* You can now customize the mappings between the current field/category/series of the primary report and corresponding field of the linked report using fields of different names, to create more dynamic link filters between the two reports with the Current Field/Category/Series = Corresponding Field condition, when you link a report to another report in both Designer and Web Report Studio.

  ![Map Current Field and Corresponding Field in Links](https://devnet.logianalytics.com/hc/article_attachments/9905903069719/corresponding-field.png)
* Server can now display reports in the current window, when creating reports on the Server Console, when creating reports in Web/Page Report Studio, and when opening reports and viewing exported outputs in Web/Page Report Studio, by setting the new option Run and Export Report in the New Window in server preferences.

  ![Create and Export Reports in Current Window](https://devnet.logianalytics.com/hc/article_attachments/9905903095575/current-window.png)
* Server administrators can now remove copies of reports that users have shared.

  ![Administrators Remove Users' Shared Reports](https://devnet.logianalytics.com/hc/article_attachments/9905903122071/remove-shared-report.png)

## Embedding Capability Enhancements

* Logi Report updates the logging implementation to use the SLF4J (Simple Logging Facade for Java) solution, enabling you to easily migrate to another logging framework, such as SimpleLogger, JUL, Logevents, reload4j, and logback.
* You can now configure your LDAP Server and manage triggers using the Rest API.

  ![Use LDAP Server and Triggers via Rest API](https://devnet.logianalytics.com/hc/article_attachments/9905931542167/rest-api.png)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9905923590551-Logi-Report-v19-2-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/7985329729687-Logi-Report-v19-1-Release-Notes)

---
title: "Imported SQL Properties"
id: 12480290993293
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480290993293-Imported-SQL-Properties
updated_at: 2026-02-25T23:48:09Z
source_host: docs-report.zendesk.com
---
# 
Imported SQL Properties

This topic describes the properties of an Imported SQL object in a catalog.

| Property Name | Description |
| --- | --- |
| Connection Name | Specifies the connection to execute the imported SQL. Data type: String |
| Description | Specifies the description of the imported SQL. Data type: String |
| Maximum Duration | Specifies the maximum elapsed time allowed to fetch data from the data source when the imported SQL runs, measured in seconds. By default, the property value is blank, meaning the time is unlimited. For more information, see Limiting the Query Run Time and Number of Records. Data type: Integer |
| Maximum Rows | Specifies the maximum number of rows to be fetched from the data source when the imported SQL runs. By default, the property value is blank, meaning the number is unlimited. For more information, see Limiting the Query Run Time and Number of Records. Data type: Integer |
| Name | Specifies the mapped name of the imported SQL in the catalog. Data type: String |
| Qualifier | Specifies the name of the database catalog for the imported SQL. Data type: String |
| Read Only | Specifies whether the imported SQL is read only. Choose an option from the drop-down list. default Select to apply the setting from the database. read & write Select to allow users to access the database in read-write mode. read only Select to allow users to access the database in read-only mode. This option can speed up the transaction of the catalog. Data type: Enumeration |
| Transaction Mode | Specifies the transaction mode for the imported SQL. Choose an option from the drop-down list. default Select to apply the setting from the database. none Select to not use transactions for the imported SQL. read uncommitted Select to allow dirty reads, non-repeatable reads, and phantom reads to occur for the imported SQL. This mode can speed up the transaction of the catalog. read committed Select to prevent dirty reads, and allow non-repeatable reads and phantom reads to occur for the imported SQL. repeatable read Select to prevent dirty reads and non-repeatable reads, and allow phantom reads to occur for the imported SQL. serializable Select to prevent dirty reads, non-repeatable reads, and phantom reads for the imported SQL. Data type: Enumeration |

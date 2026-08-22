---
title: "Connecting to My Data via REST Web Service with JSON Format"
id: 360050173433
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050173433-Connecting-to-My-Data-via-REST-Web-Service-with-JSON-Format
updated_at: 2022-11-01T11:00:51Z
---

# Connecting to My Data via REST Web Service with JSON Format

A JSON connection by a REST web service contains relational data, which is transformed from a JSON data source.

Report Designer can parse JSON data to extract the schema including the JSON metadata (i.e., JSON objects and the relation between the objects), then transform the schema to logical RDBMS tables, namely, by mapping JSON object classes to tables, and the relation to primary/foreign key columns in tables. The tables can then be added to the current connection from the transformed relational tables.

In the following example, the URI string of the sample data file is: *http://qad03.jinfonet.com.cn:8080/DataSource/RestWebService/JRDemo.json.* A parameter *pJsonUrl* is created with the value: *qad03.jinfonet.com.cn:8080/DataSource/RestWebService/JRDemo.json.*

![JSON Connection](https://devnet.logianalytics.com/hc/article_attachments/9926747084823)

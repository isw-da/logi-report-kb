---
title: "Flexible Time Zone Options"
id: 12480392025357
section: "Report Feature Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480392025357-Flexible-Time-Zone-Options
updated_at: 2026-02-25T23:47:20Z
source_host: docs-report.zendesk.com
---
# 
Flexible Time Zone Options

You can set time zone in both Report Designer and Server in a variety of ways. This topic describes the different time zone options.

On Server, you can change time zone at the server level for displaying date and time on the Server UI and in reports and parameters. 

You can also set time zone at the session level to work in one report or user session, such as in the session and the URL for running reports or dashboards, using the property rpt_timezone. 

Furthermore, in the XML data source, you can set different time zones for different date and time values. To make the time zones work on the values, you can run reports using URLs and add the parameter CustomOffset=true in the URLs, on Report Server.

For Date type fields, you can add the variable -Dreport.date.withTimezone in the server startup file JRServer.bat/JRServer.sh to control whether date type field values are time zone sensitive. The default value of this variable is false. When -Dreport.date.withTimezone=false, date values are time zone insensitive. Server doesn't convert time zone offsets and displays the raw date values fetched from data sources or the date type parameter values you type-in. When -Dreport.date.withTimezone=true, date values are time zone sensitive. Server converts them according to the time zone you specify in your server profile.

Besides, in Report Designer, you can view and export reports with value-level time zone that you set in the XML data source, by enabling the Use value time zone option.

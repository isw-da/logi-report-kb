---
title: "Configuring Server Monitor"
id: 5741385798679
section: "Logi Report Server Monitor Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741385798679-Configuring-Server-Monitor
updated_at: 2022-10-31T17:15:40Z
---

# Configuring Server Monitor

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741399649175-Using-Server-Monitor)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394406423-Monitoring-the-Status-of-Server)

# Configuring Server Monitor

This topic describes how you can configure Server Monitor by using the **Setting** tab on its home page and the **server.properties** file.

This topic contains the following sections:

* [Configuring Server Monitor on UI](#UI)
* [Configuring Server Monitor Using the server.properties File](#Property)

## Configuring Server Monitor on UI

Server Monitor displays the two tabs **Status** and **Setting** as the default page after you sign in. You can configure some of your preferences in the Setting tab. When you are at another page and want to access the Setting tab, select the root node in the left panel.

See the descriptions of the options in the **Setting** tab:

| Option | Description |
| --- | --- |
| Auto-refresh every \_ seconds | The time interval at which the status of Server Monitor gets updated automatically. |
| Show reports finished in the past \_ minutes | The time span during which the reports finished running that will be shown on the Finished Report list. |
| Maximum number of reports | The maximum number of reports to display on the Finished Report list. |
| Display the Last Login Time | Server Monitor displays the time when a user last signed in, on the top banner when you did not clear the option. |
| Submit | Select to apply your changes. |
| Reset | Select to discard your modifications and restore the tab to its default status. |

## Configuring Server Monitor Using the server.properties File

You can also configure Server Monitor using the **server.properties** file in the `<monitor_install_root>\bin` directory if you are familiar with the properties. The following table describes the properties in the **server.properties** file:

| Property | Default Value | Description |
| --- | --- | --- |
| admin.server.host | localhost | The RMI host name or IP address of the admin Server. Server Monitor checks this property value to find and connect to the admin Server. If the admin Server resides in a different computer from Server Monitor, you need to modify the value manually. |
| admin.server.port | 1129 | The RMI port number of the admin Server. Server Monitor checks this property value to connect to the admin Server. |
| httpserver.host.all | true | When the property is **true**, Logi Report Server listens on all network addresses. For Linux environment, even if httpserver.host.all=true, at most one IP address can be retrieved because of JDK's own reason. To listen on more than one IP address on Linux, or to listen on specific IP addresses instead of all network addresses, you need to set httpserver.host.all=false, and then set the IP addresses you want as the value of httpserver.host.name and separate them by a blank, for example: httpserver.host.all=false httpserver.host.name=IP1 IP2 IP3 |
| httpserver.host.name | - | When httpserver.host.all=false, you can use this property to specify IP addresses that Logi Report Server listens on. |
| httpserver.max.connections | 150 | The maximum number of connections that a standalone server can accept. A standalone server refuses new requests when the number of connections that the server is processing exceeds this number. |
| httpserver.max.handlers | 100 | The maximum number of user handlers that Logi Report Server can hold. Server can respond to requests from the client simultaneously. The number of the running requests is in inverse proportion to the speed of the response. The more requests that Server is running, the slower the speed. To improve the running speed, you can set the maximum number of user handlers to a comparatively small number. |
| httpserver.timeout | 500 | The maximum number of milliseconds that Server blocks a request from the client before refusing it. If there are still no connection handlers free after the maximum number of milliseconds has reached, Server refuses the request back to the client. |
| last.user.login.time | true | By default, Server monitor displays on the home page the time when you last signed in. |
| log.config.filename | <install\_root>\bin\LogConfig.properties | The path of the property file for configuring logs. |
| log.config.update | false | Set the property to **true** if you want to enable auto-update of logging configuration changes at runtime. Then any changes to the logging configuration file at runtime automatically take effect after the specified update interval. Otherwise, any changes to the configuration file does not take effect until you restart the Server, as the default behavior. |
| log.config.update.interval | 60000 | The interval in milliseconds for when you want to automatically update log configuration changes. This property only works after you set the **log.config.update** property to **true**. |
| monitor.cache\_control.css | public, max-age=604800 | The directives of the HTTP Request/Response header field Cache-Control for caching CSS files. |
| monitor.cache\_control.image | no-cache, must-revalidate, max-age=0 | The directives of the HTTP Request/Response header field Cache-Control for caching image files. |
| monitor.cache\_control.js | public, max-age=604800 | The directives of the HTTP Request/Response header field Cache-Control for caching JavaScript files. |
| monitor.homepage | - | The web entry of Server Monitor. The valid format is `http://<host>:<port>/<context_path>/index.jsp`. In a standalone environment, if you did not set the property value, Server Monitor uses `http://localhost:8848/monitor/index.jsp` by default, and prompts warning messages to the Console and logging destination. In the integrated environment, if you did not set this property to an explicit value, Server Monitor is not able to construct the default value. |
| monitor.jmx.htmladaptor.port | 8849 | The port that the JMX HTMLAdaptor listens to. This property depends on the **monitor.jmx.htmladaptor.startup** property. |
| monitor.jmx.htmladaptor.startup | true | Set the property to **true** if you want to start up JMX HTMLAdaptor as the default MBean viewer internally. It depends on the **monitor.jmx.startup** property. |
| monitor.jmx.startup | false | Set the property to **true** if you want to start up the JMX monitoring function and construct the Monitoring MBean when launching Server Monitor. |
| monitor.max.report.save.number | 2000 | The number of finished reports to display on the Finished Reports list. |
| monitor.max.report.save.time | 5 | The time span to display a finished report on the Finished Reports list. |
| monitor.refresh.interval | 10000 | The time interval for automatically updating the statistics of the current program status. |
| monitor.rmi.port | 1248 | The RMI port number of Server Monitor. |
| monitor.server.bin.path | <install\_root>\bin | The path of the **bin** folder that contains the startup file and properties files of Server Monitor. |
| monitor.service.port | 8848 | The service port number of Server Monitor. You can use this port to access Server Monitor. |
| server.http.output\_encoding | - | The encoding of Logi Report internal servlets. By default, jrservlet uses the JVM's encoding. |
| server.property | <install\_root>\bin\server.properties | The path of the property file for configuring the Server Monitor properties. |
| servlet.property | <install\_root>\bin\servlet.properties | The path of the property file for configuring the servlet properties. |
| web.root | <install\_root>\public\_html | The path of the **public\_html** folder that is the standalone web app folder. |

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741399649175-Using-Server-Monitor)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394406423-Monitoring-the-Status-of-Server)

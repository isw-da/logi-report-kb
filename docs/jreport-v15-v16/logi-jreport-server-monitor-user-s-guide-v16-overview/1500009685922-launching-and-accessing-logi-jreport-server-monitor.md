---
title: "Launching and Accessing Logi JReport Server Monitor"
id: 1500009685922
section: "Logi JReport Server Monitor User's Guide v16 Overview"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009685922-Launching-and-Accessing-Logi-JReport-Server-Monitor
updated_at: 2021-11-03T06:58:41Z
---

# Launching and Accessing Logi JReport Server Monitor

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711701-Installing-and-Uninstalling-Logi-JReport-Server-Monitor)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139637399/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009685962-Using-Logi-JReport-Server-Monitor)

# Launching and Accessing Logi JReport Server Monitor

This topic explains how to launch Logi JReport Server Monitor and access it from a web browser.

Below is a list of the sections covered in this topic:

* [*Starting Logi JReport Server Monitor*](#Start)
* [*Accessing Logi JReport Server Monitor Services*](#Access)

+ [*Properties in the server.properties File*](#Property)

## Starting Logi JReport Server Monitor

After you have installed Logi JReport Server Monitor, a batch file named MonitorServer.bat is generated automatically in `<install_root>\bin`. You can start Logi JReport Server Monitor by running this batch file.

To successfully start Logi JReport Server Monitor, these requirements should be met:

* Copy rmi.auth from `<adminserver_install_root>\bin` of the admin server to `<monitor_install_root>\bin`, or remove rmi.auth from `<adminserver_install_root>\bin`, or add `-Djrs.rmi.auth_file=%authFileName%` to MonitorServer.bat to specify the authentication file.
* Make sure that the server.rmimonitor.enable property in the server.properties file in the `<adminserver_install_root>\bin` directory is set to true. The default value is true.
* If the admin server and Monitor are installed in different computers, you need specify the right host and port of the admin server in Monitor side via the two properties in the server.properties file in the `<monitor_install_root>\bin` directory before starting Logi JReport Server Monitor:

  [admin.server.host](#adminhost)=The RMI host name or IP address of the admin server.

  [admin.server.port](#adminport)=The RMI port number of the admin server.

  The default values of these two properties are for the admin server which is installed in the same computer.

  **Note:** The server.properties file is generated when you run MonitorServer.bat for the first time after installation. The step does not require that the Monitor is started and connected to the admin server successfully.
* The admin server is started successfully. It does not matter whether you start the admin server first or the Monitor first.

## Accessing Logi JReport Server Monitor Services

After Logi JReport Server Monitor is started successfully, you can take either of the following ways to access Logi JReport Server Monitor via browsers:

**By URL**

Use the service port number specified in the server.properties file to access the services of Logi JReport Server Monitor. The default format of the accessing URL is: http://MonitorHost:MonitorServicerPort/monitor/index.jsp. For example, if Logi JReport Server Monitor and Logi JReport Server are installed on one computer, you can use `http://localhost:8848.`

**From Logi JReport Server UI**

You can also access Logi JReport Server Monitor by selecting the Monitor link on the Logi JReport Server console > Administration > Other drop-down menu. To do this, you need make sure:

* The web.monitor.link.enable property in the server.properties file in `<server_install_root>\bin` is set to true. The default value is true.
* You are an administrator or have the privilege to access the Administration page of the server console.

### Properties in the server.properties File

The following details the properties in the server.properties file which is located in the `<monitor_install_root>\bin` directory:

| Property | Default Value | Description |
| --- | --- | --- |
| admin.server.host | localhost | The RMI host name or IP address of the admin server. Logi JReport Server Monitor will check this property value to find and connect to the admin server. If the admin server resides in a different computer from the monitor, you need modify the value manually. |
| admin.server.port | 1129 | The RMI port number of the admin server. Logi JReport Server Monitor will check this property value to connect to the admin server. |
| log.config.update | false | Specifies to enable auto-update of logging configuration changes (by manually modifying the configuration file) at runtime. If set to true, any changes to the logging configuration file at runtime will automatically take effect after the specified update interval. Otherwise, any changes to the configuration file will not take effect until you restart the Server. |
| log.config.update.interval | 60000 | Specifies the interval value (in milliseconds) for when logging configuration changes will be auto-updated. This property will only function after the log.config.update property has been set to true. |
| monitor.homepage | - | Specifies the web entry of Logi JReport Server Monitor. The valid format is `http://<host>:<port>/<context_path>/index.jsp`. In a standalone environment, if there is no value set to this property, Logi JReport Server Monitor uses `http://localhost:8848/monitor/index.jsp` by default, and will prompt warning messages to the Console and logging destination. In the integrated environment, if this property has not been set to an explicit value, Logi JReport Server Monitor will not be able to construct the default value. |
| monitor.jmx.htmladaptor.port | 8849 | The port that the JMX HTMLAdaptor listens to. This property depends on the monitor.jmx.htmladaptor.startup property. |
| monitor.jmx.htmladaptor.startup | true | Specifies whether to start up JMX HTMLAdaptor as the default MBean viewer internally. It depends on the monitor.jmx.startup property. |
| monitor.jmx.startup | false | Specifies whether to start up the JMX monitoring function and construct the Monitoring MBean when launching Logi JReport Server Monitor. |
| monitor.max.report.save.number | 50 | The number of finished reports to be shown on the Finished Reports list. |
| monitor.max.report.save.time | 5 | The time span that a finished set should be shown on the Finished Reports list. |
| monitor.refresh.interval | 2000 | The time interval for automatically updating the statistics of the current program status is automatically updated. |
| monitor.rmi.port | 1248 | The RMI port number of Logi JReport Server Monitor. |
| monitor.service.port | 8848 | The service port number of Logi JReport Server Monitor. You can use this port to access Server Monitor. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711701-Installing-and-Uninstalling-Logi-JReport-Server-Monitor)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139637399/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009685962-Using-Logi-JReport-Server-Monitor)

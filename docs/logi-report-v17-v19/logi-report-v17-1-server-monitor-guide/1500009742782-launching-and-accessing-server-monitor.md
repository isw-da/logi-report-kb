---
title: "Launching and Accessing Server Monitor"
id: 1500009742782
section: "Logi Report v17.1 Server Monitor Guide"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009742782-Launching-and-Accessing-Server-Monitor
updated_at: 2021-07-24T00:49:41Z
---

# Launching and Accessing Server Monitor

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742722-Installing-and-Uninstalling-Server-Monitor)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742802-Using-Server-Monitor)

# Launching and Accessing Server Monitor

This topic introduces how you can launch Server Monitor and access it from a web browser.

This topic contains the following sections:

* [Starting Server Monitor](#Start)
* [Accessing Server Monitor Services](#Access)

## Starting Server Monitor

After you have installed Server Monitor, it generates a batch file **MonitorServer.bat** automatically in `<install_root>\bin`. You can start Server Monitor by running this batch file.

To successfully start Server Monitor, you should meet these requirements:

* Copy **rmi.auth** from `<adminserver_install_root>\bin` of the admin Server (the Server you want to monitor) to `<monitor_install_root>\bin`, or remove rmi.auth from `<adminserver_install_root>\bin`, or add `-Djrs.rmi.auth_file=%authFileName%` to **MonitorServer.bat** to specify the authentication file.
* Make sure that the **server.rmimonitor.enable** property in the **server.properties** file in the `<adminserver_install_root>\bin` directory is set to **true**. The default value is **true**.
* If you installed the admin Server and Server Monitor on different computers, you need to specify the right host and port of the admin Server in Server Monitor side via the two properties in the **server.properties** file in the `<monitor_install_root>\bin` directory before starting Server Monitor:

  [admin.server.host](https://devnet.logianalytics.com/hc/en-us/articles/1500009742842-Configuring-Server-Monitor#adminhost)=The RMI host name or IP address of the admin Server.

  [admin.server.port](https://devnet.logianalytics.com/hc/en-us/articles/1500009742842-Configuring-Server-Monitor#adminport)=The RMI port number of the admin Server.

  The default values of these two properties are for the admin Server that you installed in the same computer.

  **![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)**Server Monitor generates the **server.properties** file when you run **MonitorServer.bat** for the first time after installation.
* You started the admin Server.

## Accessing Server Monitor Services

After you start the Server Monitor, you can access Server Monitor via browsers in one of these ways:

**By URL**

Use the service port number from your server.properties file to access the services of Server Monitor. The default format of the accessing URL is: `http://MonitorHost:MonitorServicerPort/monitor/index.jsp`. For example, if you installed Server Monitor and Server on one computer, you could use `http://localhost:8848.`

**From Server UI**

You can also access Server Monitor by selecting the **Monitor** link on the Server Console > Administration > Other drop-down menu. To do this, you need make sure that:

* The **web.monitor.link.enable** property in the server.properties file in `<server_install_root>\bin` is set to **true**. The default value is **true**.
* You are an administrator or have the privilege to access the **Administration** page of the Server Console.

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742722-Installing-and-Uninstalling-Server-Monitor)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742802-Using-Server-Monitor)

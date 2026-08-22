---
title: "Example 1: Setting Up a Simple Report Server Cluster"
id: 28891532266765
section: "Report Server Cluster Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891532266765-Example-1-Setting-Up-a-Simple-Report-Server-Cluster
updated_at: 2026-02-26T02:11:12Z
source_host: docs-report.zendesk.com
---
# 
Example 1: Setting Up a Simple Report Server Cluster 

This topic describes how you can configure a simple Report Server Cluster by modifying the configuration options in the Console of each Report Server, as an administrator.

Example description:

- Set up a simple Report Server Cluster via the Server Console. Assume that Report Server Monitor has been installed on your computer. 

- The cluster consists of two copies of Report Server on one computer. 

- The cluster uses one server DBMS.

- The cluster uses shared directories for resources, so no resource copies are required. 

Take the following steps to set up the cluster:

- Install the two Report Servers respectively to C:\LogiReport\Server1 and C:\LogiReport\Server2 using the cluster enabled license key. 

- Launch the Report Server installed to C:\LogiReport\Server2.  

- 
Access the Server Console of Server2 using port 8888 as an administrator.

- On the system toolbar, navigate to Administration > Configuration > Service. Server displays the Service page.

- Set Port to 8883 to make it different from that of Server1. You can use any port number available on your system. 

- On the system toolbar, navigate to Administration > Configuration > Cluster > Configuration. Server displays the Configuration page. 

- Specify a cluster name.

- Select Enable Cluster.

- Select Save to enable the cluster. 

- Restart the Report Server you installed to C:\LogiReport\Server2.

- Sign in to the Server Console of Server2 using the port 8883 you specified in step 3 (http://localhost:8883) as an administrator.

- Navigate to the Administration > Configuration > Cluster > Configuration page.

- Leave Load Balancer Type as Round Robin.

- Select Cluster Scheduler Lease to enable lease for the cluster.

- Set the active count, valid time, and check interval for the cluster scheduler lease. 

- Change the Cluster Storage History, Realm and CRD Result Number of Copies to 1. We just use one resource directory.

- Keep the default value 2 for Cluster Memory Storage Number of Copies, thus 2 memory copies will be shared in the cluster.

- Select Notify via E-mail When a Server Is Down.

- In the E-mail Address text box, type the email addresses of the people to whom you want to send a notification email. 

- Keep the default values for Properties Directory, Realm Directory, Resource Root, History Directory, and Temporary Files Directory.

- Type the IP address or host name of Server2 in the Server's RMI Host text box.

- Type the port number in the Server's RMI Port text box.
    The port is the RMI port of the clustered server. The default port number is 1129. If two or more Report Servers started on one machine, the RMI port number of each clustered server must be a unique one, in order to avoid port conflict.

In this example, we change the port number to 1130, since the other server will use the default port number 1129.

- Select Save to accept all the changes.
			

- Shut down the server.

- Edit C:\LogiReport\Server2\bin\dbconfig.xml and remove the lines with auto-start-derbyservice. We only want Server1 to start the server DBMS since we will always use the Server1 database. 

- Launch the Report Server you installed to C:\LogiReport\Server1.

- Sign in to its Server Console (http://localhost:8888) as an administrator.

- On the system toolbar, navigate to Administration > Configuration > Cluster > Configuration. 

- Use the same cluster name as Server2, thus making Server1 join the existing cluster. 

- Select Enable Cluster.

- Select Save to enable the cluster. 

- Restart the Report Server you installed to C:\LogiReport\Server1.

- Sign in to the Server Console again.

- Go to the Administration > Configuration > Cluster > Configuration page, configure Server's RMI Host and Server's RMI Port. Remember to keep Server's RMI Port to its default value 1129. 

- Select Save to accept all settings.

- Shut down Server1.

- Copy rmi.auth in C:\LogiReport\Server1\bin to C:\LogiReport\Server2\bin. This authorizes RMI between the two systems.

- Edit the server.properties file in C:\LogiReport\Server2\bin to remove cluster.member.id. Server2 will recreate the ID with a unique number when it restarts.

- Start the server Derby DBMS service by double-clicking the startNetworkServer.bat file in C:\LogiReport\Server1\derby\bin.

- Restart Server1 and Server2.

- Access the Server Console of the first server using port 8888 as an administrator.

- Submit a scheduled task. You see the newly scheduled task on the Scheduled tab.

- Sign in to the Server Console of the second server as an administrator.

- 
Create a new user Tom in the Administration > Security > User page.

- Access the Server Console of the second server using port 8883 as Tom.

- Submit another scheduled task.

- When you schedule to publish a report on a clustered server to disk, you should first specify a disk in your file system and make sure that every node in the cluster has the same disk name mapping to the same physical location. Then Server saves the publishing report directly to the disk you specify. 

- You can only view scheduled tasks that you have submitted.

- From the Server Console of the clustered Report Servers, you can only view completed tasks that you have submitted.

- If there are more than two clustered servers in the cluster, then after you shut down one server, all the scheduled tasks running on this server will run on other servers.

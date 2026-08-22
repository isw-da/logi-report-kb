---
title: "Using and Upgrading Logi Report Server on Docker"
id: 4420461818007
section: "Starting, Accessing, and Shutting Down Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4420461818007-Using-and-Upgrading-Logi-Report-Server-on-Docker
updated_at: 2022-01-27T07:58:15Z
---

# Using and Upgrading Logi Report Server on Docker

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690639639-Shutting-Down-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683578647-Configuring-Server-v18)

# Using and Upgrading Logi Report Server on Docker

This topic describes how to pull a Logi Report Server docker image and access Logi Report Server, as well as run, upgrade, and remove a Logi Report Server container.

This topic contains the following sections:

* [Pulling a Server Docker Image and Accessing Server in Windows](#Pull)
* [Upgrading a Server Container](#Upgrade)
* [Stopping and Removing a Server Container](#Stop)

## Pulling a Server Docker Image and Accessing Server in Windows

![](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)To use a Server docker image, you
must have the associated license key of the Server version. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

1. Download and install the latest version of Docker from this site: [Docker download](https://docs.docker.com/get-docker/).
2. Start **Docker Desktop**.
3. Open the Command Prompt.
4. Pull a Logi Report Server docker image from [Docker Hub](https://hub.docker.com/r/logianalytics/logireport-server).

   ```
   docker pull logianalytics/logireport-server[:image_tag]
   ```

   To pull the Server image "latest", you can specify a simpler command line instead.

   ```
   docker pull logianalytics/logireport-server
   ```

   You can see all available image tags for Logi Report Server starting from v15.5 to the latest release in the Docker Hub. For each Server version, you may find its docker images based on Oracle JDK 8, 11, or 17. From an image tag name you can figure out the Server version (18.2.2 or 18.2-sp2 means v18.2 Service Pack 2), the date and time when the Server version was released (B202112240214 means Nov. 22, 2021 02:14), or the JDK version that the Server uses (18.2.2-jdk11 uses JDK 11). When a line contains more than one tag name, they all point to the same Server image.
5. Start the Server container.

   ```
   docker run -itd -p 8888:8888/tcp --name logireport_server logianalytics/logireport-server[:image_tag]
   ```
6. You can inspect the startup status of the container.

   ```
   docker logs -f logireport_server
   ```
7. Access the Server instance locally via <http://localhost:8888/>.
8. Type your user ID and license key for Server.

   ![Update Server License](https://devnet.logianalytics.com/hc/article_attachments/4420447350039/config_license2.gif)
9. Select **Submit**.
   Server displays the license information.
10. Access <http://localhost:8888/> again.
11. Type your username and password to sign on to Server.
12. If you want to view Server information in the container, manually stop/restart Server, clear Server logs, or manually configure Server property files LogConfig.properties/server.properties, make the running Server container work as standalone installed server.

    ```
    docker exec -it -w /opt/LogiReport/Server logireport_server bash
    ```

## Upgrading a Server Container

1. Backup your data in the Server container.

   ```
   # Stop server processes of the previous version in the server container (Suppose that report_server is the container name)  
   docker exec report_server /opt/LogiReport/Server/bin/stopServer.sh  
     
   # Backup the previous version  
   docker exec -w /opt/LogiReport/Server/bin report_server bash -xc '  
   ./DBMaintain.sh -Bsystemtables:systemtables.dat  
   ./DBMaintain.sh -B0realmtables:realmtables.dat  
   ./DBMaintain.sh -Bprofiling:profiling.dat'  
   docker cp report_server:/opt/LogiReport/Server ./Server_old_version
   ```
2. Run the new version of the server container:

   ```
   # Create a new version container.  
   docker create --name new_server -v /opt/LogiReport/Server logianalytics/logireport-server[:image_tag]  
     
   # Copy the new server content.  
   docker run --rm --volumes-from new_server -v `pwd`:/tmp/workspace ubuntu cp -rp /opt/LogiReport/Server /tmp/workspace/Server_new  
     
   # Upgrade the server container.  
   sudo rm Server_new/bin/{jslc.dat,setenv.sh}  
   for i in `ls -A Server_new/bin/*.{properties,xml}|grep -Ev '(content-type|servlet|LogConfig|mapping).properties|makewar.xml'`  
   do sudo rm -f $i  
   done  
   docker cp Server_old_version/bin/systemtables.dat report_server:/tmp  
   docker cp Server_old_version/bin/realmtables.dat report_server:/tmp  
   docker cp Server_old_version/bin/profiling.dat report_server:/tmp  
   docker cp Server_new report_server:/opt/LogiReport  
   docker exec -w /opt/LogiReport/Server_new report_server bash -c 'cp -rpf ./* ../Server/'  
   docker exec -w /opt/LogiReport report_server rm -rf Server_new  
   docker exec -w /opt/LogiReport/Server/bin report_server bash -xc '  
   ./DBMaintain.sh -Rsystemtables:systemtables.dat  
   ./DBMaintain.sh -R0realmtables:realmtables.dat  
   ./DBMaintain.sh -Rprofiling:profiling.dat'  
     
   # Restart the upgraded container.  
   docker restart report_server  
     
   # Remove the created new_server container which is for temporary use.  
   docker rm -v new_server  
   sudo rm -rf Server_new
   ```

## Stopping and Removing a Server Container

You should stop and remove the Server container once you are done.

Stop the Server container:

```
docker stop logireport_server
```

Remove the Server container from your computer:

```
docker rm -v logireport_server
```

Remove the Server image:

```
logianalytics/logireport-server[:image_tag]
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690639639-Shutting-Down-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683578647-Configuring-Server-v18)

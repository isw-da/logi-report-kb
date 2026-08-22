---
title: "Publishing Resources from One Server to Another"
id: 1500009718562
section: "Work With APIs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718562-Publishing-Resources-from-One-Server-to-Another
updated_at: 2021-07-25T07:20:22Z
---

# Publishing Resources from One Server to Another

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009744441-Using-RMI-in-Logi-Report-Server)[Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744541-Working-with-Resource-Versions)

# This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Publishing Resources from One Server to Another

Using the [TargetServerManager](#TargetServerManager) and [TargetServer](#TargetServer) objects provided in the jet.server.api package of the Server API, you can [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources#ToServer) in the resource tree of a Logi Report Server (source server) to another Logi Report Server (target server).

## TargetServerManager

The TargetServerManager object manages the TargetServer objects. You can get it using the method *RptServer.getTargetServerManager()*.

See the methods contained in TargetServerManager:

* String createTargetServer(user, connectionProp)  
  Creates the TargetServer object for the specified user using the designated connection properties. Returns the ID for the newly created TargetServer
  object; or throws exception when
  connectionProp is invalid.
  + user - The user name used to log onto the target server.
  + connectionProp - A property that contains the connection information.
* TargetServer getTargetServer(ID)  
  Gets the TargetServer object of the specified ID.
  Returns null if there isn't the
  TargetServer object for the current user; or throws exception when the
  TargetServer object is invalid.
  + ID - The ID of the TargetServer object.
* void deleteTargetServer(ID)  
  Deletes the TargetServer object of the specified ID.
  + ID - The ID of the TargetServer object.
* Properties getConnectionProp(ID)  
  Gets the connection properties stored in the specified TargetServer object.
  + ID - The ID of the TargetServer object.

## TargetServer

The TargetServer object indicates the target server. It contains user name and connection properties. Each user name corresponds to one TargetServer object.

See the methods contained in TargetServer:

* void connect()  
  Logs onto the target server where to publish resources and creates a new session.
* void disconnect()  
  Logs out from the target server and removes the session.
* String getFolderTree(permissions)  
  Gets the JSON string of the target server resource folder tree according to the specified permissions.
  + permission - The permissions the logged-in user has on the target server folders.
* boolean resourceExists(path)  
  Returns
  whether the specified path node exists on the target server resource tree.
  + path - The path on the target server resource tree.
* String getPermission(path)  
  Gets the binary string of the permissions the logged-in user has on the specified path.
  + path - The path on the target server resource tree.
* void setPermission(path, permissions)  
  Sets permissions for the logged-in user on the specified target server path.
  + path - The path on the target server resource tree.
  + permissions - The permissions the logged-in user has on the specified path.
* void addResourceFile(path, resourceName, fromFile, properties, permissions)  
  Publishes the specified resource file to the designated path on the target server.
  + path - The path on the target server resource tree where to publish resources.
  + resourceName - The node name for the to-be-published resources on the target server.
  + fromFile - The compressed file that contains the resources you want to publish.
  + properties - The properties of the to-be-published resources.
  + permissions - The user permissions for the to-be-published resources.
* void createFolder(path, resourceName, properties, permissions)  
  Creates folder on the target server.
  + path - The path on the target server resource tree where to create the folder.
  + resourceName - The name of the new folder.
  + properties - The properties of the new folder.
  + permissions - The user permissions for the new folder.
* Properties getResourceProperties(path)  
  Gets the properties of the specified path on the target server.
  + path - The path on the target server resource tree.
* void setResourceProperties(path, properties)  
  Sets properties for the specified path on the target server.
  + path - The path on the target server resource tree.
  + properties - The properties of the resource path.
* void deleteResource(path)  
  Deletes the specified path from the target server.
  + path - The path on the target server resource tree.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009744441-Using-RMI-in-Logi-Report-Server)[Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744541-Working-with-Resource-Versions)

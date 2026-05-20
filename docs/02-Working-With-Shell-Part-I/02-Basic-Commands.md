# Basic Linux Commands

- Take me to the [Video Tutorial](https://kodekloud.com/topic/basic-linux-commands-3/)

In this section, we will take a look at basic linux commands 
- Specifically related to navigation and creating new files and directories.
- We will do this by completing a simple task using a linux shell.

#### Our goal is to create a directory structure, the top most directory which is **`/home/michael`** which is already created as it as a home directory but everything else underneath has to be created. 

![mkdir_cd_working_with_shell_I](../../images/mkdir_cd_working_with_shell_I.PNG)

To print the present working directory. Run **`pwd`** command
```shell
$ pwd
```

To see the contents of the directory. Run **`ls`** command
```shell
$ ls 
````

To make (or) create a directory. Run **`mkdir`** command
```shell
$ mkdir Asia
```

To make (or) create multiple directories. Run **`mkdir`** command followed by **`<directory_name1> <directory_name2> .. <directory_nameN>`**
```shell
$ mkdir Europe Africa America
```

To change a directory from the current directory. Run **`cd <directory_name>`**
```shell
$ cd Asia
```

To recursively created directories. Run **`mkdir -p <directory_name1>/<sub_directory_of_name1>`**
```shell
$ mkdir -p India/Mumbai
```

To go back to one directory up. Run **`cd ..`**
```shell
$ cd ..
```

To go back directly to a home directory of the current user from any location in the system. Run **`cd`**
```shell
$ cd
```

#### Lets now look at absolute path and relative path



![Absolute_and_relative_path_working_with_shell_I](../../images/Absolute_and_relative_path_working_with_shell_I.PNG)

**Difference Between Absolute and Relative Path**

- **Absolute Path** : An absolute path is defined as specifying the location of a file or directory from the root directory(/).
- **Relative Path** : Relative path is defined as the path related to the present working directly(pwd).

To change to a directory with absolute path. Run **`cd <directory_path>`**
```shell
$ cd /home/michael
```

To Change to a directory with relative path. Run **`cd <directoryName>`**
```shell
$ cd Asia
```

#### Lets now take a look at alternatives to the **`cd`** command

![pushd_popd](../../images/pushd_popd.PNG)

Alternative to the **`cd`** is the **`pushd\popd`** command. To change directory using pushd, run **`pushd <directory_name>`**
```shell
$ pushd /etc
```

You can change to subdirecties under /etc as many times as you wish
```shell
$ pushd /var
$ pushd /tmp
$ pwd
/etc/var/tmp
```

To return back to origin directory(say your home directory), use the **`popd`** command
```shell
$ popd
```

#### Now lets move on to look some more basic commands in linux. To learn these commands we will make use of the same directory structure as before, however now there are some new files and directories added as shown in the diagram. The goal of this task is to make sure the directory structure looks like the below diagram .

![before_after_commands](../../images/before_after_commands.PNG)

To move file or directory. Run **`mv <source> <destination>`** command
```shell
$ mv /home/michael/Europe/Morocco /home/michael/Africa/ (Absolute path)
$ mv Europe/Morocco Africa/ (Relative Path)
```

To rename a directory. Run **`mv <oldname> <newname>`** command
```shell
$ mv Asia/India/Munbai Asia/India/Mumbai
```

To copy a file to a directory. Run **`cp <filename> <destination_directorypath>`** command
```shell
$ cp Asia/India/Mumbai/City.txt Africa/Egypt/Cairo
```

To delete a file from a directory. Run **`rm /path/<filename>`** command
```shell
$ rm Europe/UK/London/Tottenham.txt
```

To copy a directory recursively. Run **`cp -r <sourcepath> <destinationPath>`** command
```shell
$ cp -r Europe/UK Europe/UnitedKingdom
```

To print the content of a file. Run **`cat /path/to/<filename>`** command
```shell
$ cat Asia/India/Mumbai/City.txt
```

To add a content to a file with cat(redirect) . Run **`cat > /path/to/<filename>`** command
```shell
$ cat > Africa/Egypt/Cairo/City.txt
  Cairo
  `Type Ctrl + d from keyboard`
```

To create an empty file. Run **`touch /path/to/filename`** command
```shell
$ touch /home/michael/Asia/China/Country.txt
```

To see the content of a file in a scrollable manner. Run **`more /path/to/filename`** command <-- not recommended for large files
```shell
$ more new_file.txt
```

To see the content of a file and navigate throught the file. Run **`less /path/to/filename`** command
```shell
$ less new_file.txt
```

To get the long list of files and directories. Run **`ls -l`** command
```shell
$ ls -l
```

To list all files including the hidden. Run **`ls -la`** command
```shell
$ ls -a
```

To list all the files in the order they were modified. Run **`ls -lt`** command
```shell
$ ls -lt
```

To list all the files form oldest to newest. Run **`ls -ltr`** command
```shell
$ ls -ltr
```


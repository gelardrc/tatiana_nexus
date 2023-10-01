# tatiana_nexus
____________________________________________________________________

Dependencias

* Real_sense_description * --> https://github.com/issaiass/realsense2_description/tree/master 

* Real_sense_plugin * -- > https://github.com/issaiass/realsense_gazebo_plugin.git

* Real_sense_package * -- > https://github.com/IntelRealSense/realsense-ros.git

* nexus_robot * -- > https://github.com/RBinsonB/nexus_4wd_mecanum_simulator.git

obs : deletar a pasta real_sense_description do real_sense_package e manter somente a do git do issaiass 

_______________________________________________________________________

Instalar o pacote tatiana_nexus  ( sugiro criar outro catkin workspace )

> mkdir -p catkin_tatiana/src
> 
> cd catkin_tatiana
> 
> catkin_make
> 
> cd src
>  
'Instale as dependencias agora e faça o lance de apagar a pasta do description, git clone (e os links acima)'
> 
> cd ..
>
> catkin_make

`esse catkin_make é o que adiciona a biblioteca .h que o cara criou para a movimentação. O caminho desse arquivo é sua_work_space/src/nexus_4wd_mecanum_simulator/nexus_4wd_mecanum_gazebo/include/nexus_4wd_mecanum_gazebo/nexus_ros_force_based_move.h `
 
>
> cd src/
>
> git clone https://github.com/gelardrc/tatiana_nexus.git
>
> source ../devel/setup.bash


___________________________________________________________________________________________

Executando o pacote tatiana_nexus 

> roslaunch tatiana_nexus world.launch
>
`em outra guia de o comando abaixo`
> source devel/setup.bash
> 
> roslaunch tatiana_nexus robot.launch


____________________________________________________________________________________________
Abrindo o mundo substation

`Copie os arquivos da pasta models, para a pasta ~/.gazebo/models, depois execute:`

>cd ~/tatiana_nexus

> roslaunch tatiana_nexus world.launch world:=$(pwd)/src/tatiana_nexus/worlds/substation_2.world

`Demora um pouco `

_____________________________________________________________________________________________
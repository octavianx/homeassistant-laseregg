


# homeassistant-laseregg

**This code is deprecated**   
Updated in Dec,2022
It is deprecated for kaiterra has updated laseregg security measure that it will neeed a API Key to access the laseregg data.
And homeassistant has officially supported laseregg. https://www.home-assistant.io/integrations/kaiterra/

Be aware that in the Kaiterra dashboard, you need to search `article` in the source code to identify the UUID for each of your
device.



This a component for laseregg to be adapted to homeassistant.

## Cause: 

The original device of laseregg v1 donot provied the ability to be 
controlled via home-assistant nor the Apple HomeKit connection.

The homebridge plugin has been created to provide Apple homekit 
capability, however the best practice is  connect all the devices
via home-assistant, for a centeralize control, and provie a 
portal to homekit via homebridge-homeassistant.



本代码由用于在homeassitant 上提供对第一代镭豆设备(laser egg)的支持.
laser egg是一个激光计数为基础的空气粒子计数器，用于采样PM2.5/PM10
指数。




homeassistant
homebridge
Apple homekit



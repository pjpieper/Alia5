<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>480</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>70</y>
      <width>671</width>
      <height>321</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="1" column="0">
      <widget class="QPushButton" name="LedButton">
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset>
         <normaloff>Icons/IRLED_Icon.png</normaloff>Icons/IRLED_Icon.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>78</width>
         <height>78</height>
        </size>
       </property>
       <property name="flat">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="1" column="3">
      <widget class="QPushButton" name="MapsButton">
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset>
         <normaloff>Icons/gougle.png</normaloff>Icons/gougle.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>78</width>
         <height>78</height>
        </size>
       </property>
       <property name="flat">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QPushButton" name="SpotifyButton">
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset>
         <normaloff>Icons/spotrify.png</normaloff>Icons/spotrify.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>78</width>
         <height>78</height>
        </size>
       </property>
       <property name="flat">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="0" column="3">
      <widget class="QPushButton" name="DoomButton">
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset>
         <normaloff>Icons/doom.png</normaloff>Icons/doom.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>78</width>
         <height>78</height>
        </size>
       </property>
       <property name="flat">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="1" column="2">
      <widget class="QPushButton" name="RasButton">
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset>
         <normaloff>Icons/RasIcon.png</normaloff>Icons/RasIcon.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>78</width>
         <height>78</height>
        </size>
       </property>
       <property name="flat">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="0" column="4">
      <widget class="QPushButton" name="DiscordButton">
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset>
         <normaloff>Icons/discordy.png</normaloff>Icons/discordy.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>78</width>
         <height>78</height>
        </size>
       </property>
       <property name="flat">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QPushButton" name="CamButton">
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset>
         <normaloff>Icons/camera.png</normaloff>Icons/camera.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>78</width>
         <height>78</height>
        </size>
       </property>
       <property name="flat">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="0" column="0">
      <widget class="QPushButton" name="WireSharkButton">
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset>
         <normaloff>Icons/WS_PNG.png</normaloff>Icons/WS_PNG.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>78</width>
         <height>78</height>
        </size>
       </property>
       <property name="flat">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item row="0" column="2">
      <widget class="QPushButton" name="VpnButton">
       <property name="text">
        <string/>
       </property>
       <property name="icon">
        <iconset>
         <normaloff>Icons/protonvpn.png</normaloff>Icons/protonvpn.png</iconset>
       </property>
       <property name="iconSize">
        <size>
         <width>78</width>
         <height>78</height>
        </size>
       </property>
       <property name="flat">
        <bool>true</bool>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>-140</x>
      <y>-20</y>
      <width>1011</width>
      <height>511</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>Backgrounds/146770.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <zorder>label</zorder>
   <zorder>gridLayoutWidget</zorder>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

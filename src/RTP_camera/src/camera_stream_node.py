#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def publish_camera_stream():
    rospy.init_node('camera_stream_node')
    image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)
    bridge = CvBridge()
    
    cap = cv2.VideoCapture("rtsp://192.168.100.100:554/cam0_0")
    
    if not cap.isOpened():
        rospy.logerr("Unable to open RTPstream")
        return
    
    
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret : 
            image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            image_pub.publish(image_msg)

    cap.release()
    
if __name__ == '__main__' :
    try:
        publish_camera_stream()
    except rospy.ROSInterruptException:
        pass

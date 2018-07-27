# -*- coding: utf-8 -*-


def get_params():
    return {
        'bridge': {
            'topics': {
                'cmd_sub': '/turtlebot3_bridge/cmd',
                'attrs_pub': '/turtlebot3_bridge/attrs',
            },
            'thresholds': {
                'send_delta_millisec': 100,
            },
        },
        'turtlebot3': {
            'rate_hz': 10,
            'circle': {
                'velocities': {
                    'x': 0.1,
                    'z': 0.4,
                },
                'thresholds': {
                    'dist_meter': 0.1,
                    'angular_rad': 0.02,
                },
            },
            'polygon': {
                'velocities': {
                    'x': 0.2,
                    'z': 0.2,
                },
                'edge': {
                    'length_meter': 0.4,
                },
                'thresholds': {
                    'dist_meter': 0.01,
                    'angular_rad': 0.02,
                },
            },
            'unit': {
                'length_meter': 0.1,
                'theta_rad': 0.01,
            },
            'topics': {
                'cmd_pub': '/cmd_vel',
                'odom_sub': '/odom',
            },
        },
    }

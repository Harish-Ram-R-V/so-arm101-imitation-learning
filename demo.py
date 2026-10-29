import tkinter as tk
from lerobot.robots.so_follower import SO101FollowerConfig, SO101Follower

class ArmControllerUI:
    def __init__(self, root, port):
        self.root = root
        self.root.title("SO-ARM 101 Testing UI")
        
        # Intercept the window close button to safely turn off motor torque
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        config = SO101FollowerConfig(port=port, id="arm_ui_test")
        self.robot = SO101Follower(config)
        self.robot.connect()
        
        self.joints = ["Shoulder Pan (Base)", "Shoulder Lift", "Elbow Flex", "Wrist Flex", "Wrist Roll", "Gripper"]
        self.sliders = []
        
        for name in self.joints:
            frame = tk.Frame(root)
            frame.pack(fill=tk.X, padx=15, pady=5)
            tk.Label(frame, text=name, width=18, anchor='w').pack(side=tk.LEFT)
            
            # The 'command' parameter triggers real-time updates as you drag
            slider = tk.Scale(
                frame, from_=-1.0, to=1.0, resolution=0.01, 
                orient=tk.HORIZONTAL, length=400, command=self.send_commands
            )
            slider.pack(side=tk.LEFT, expand=True)
            self.sliders.append(slider)
            
    def send_commands(self, _=None):
        motor_names = [
            "shoulder_pan", "shoulder_lift", "elbow_flex", 
            "wrist_flex", "wrist_roll", "gripper"
        ]
        action_dict = {}
        for i, name in enumerate(motor_names):
            action_dict[f"{name}.pos"] = self.sliders[i].get()
            
        self.robot.send_action(action_dict)

    def on_closing(self):
        # Disconnect safely to release servo torque before destroying the window
        self.robot.disconnect()
        self.root.destroy()

if __name__ == "__main__":
    app_window = tk.Tk()
    ui = ArmControllerUI(app_window, port="COM4") 
    app_window.mainloop()
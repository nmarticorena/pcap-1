from estimation.real.domain import ArmType

from .sim2_real_kinova_tree_tactile_voxel_reach import Sim2RealKinovaTreeTactileVoxelReach


class Sim2RealFrankaTreeTactileVoxelReach(Sim2RealKinovaTreeTactileVoxelReach):
    """Simulation-only PCAP tree-reaching task for the Franka Panda."""

    robot_name = "franka"
    robot_asset_key = "assetFileNameFranka"
    num_policy_dofs = 7
    robot_default_dof_values = [1.157, -1.066, -0.155, -2.239, -1.841, 1.003, 0.469, 0.035, 0.035]
    robot_cont_dof_indices = []
    robot_dof_damping_values = [80, 80, 80, 80, 80, 80, 80, 100, 100]
    robot_dof_friction_values = [1e-2] * 9
    robot_speed_scale_indices = [7, 8]
    hand_body_name = "panda_link7"
    left_finger_body_name = "panda_leftfinger"
    right_finger_body_name = "panda_rightfinger"
    flip_visual_attachments = True
    arm_type = ArmType.franka
    max_norm_impact_cf = 800.0
    supports_real = False

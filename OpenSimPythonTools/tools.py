def btk_loadc3d(file, grw_threshold):
    """
    % function [marker_data, analog_data, fp_data, sub_info] = btk_loadc3d(file)
    %
    % Function to load the data from a c3d file into the structured array data.
    % The file may be excluded if you wish to choose it from a windows dialog
    % box
    %
    % INPUT -
    %           file - the file path that you wish to load (leave blank to
    %               choose from a dialog box)
    %           threshold - the force threshold for calculating the GRW
    %           (default 5 N)
    %
    % OUTPUT - all structured arrays containing the following data
    %           marker_data - any calculated data from the reconstructed C3D
    %               file including marker trajectories  and any calculated angles,
    %               moments, powers or GRF data
    %           analog_data - analog data (often sampled at a higher rate) including
    %               force plate data and EMG data that might be collected.
    %           grw_data - structure with the position magnitude of ground
    %               reaction force vector and moments relative to the global
    %               cooridinate system
    %           fp_info - structure with the force outputs from the force
    %               plates including the ground reaction wrench (force vector
    %               calculated in the global axis frame) and relevant
    %               sampling and forceplate position information
    %           sub_info - extra data from the C3D file if it exists, inlcuding
    %               height and weight etc.
    %
    %
    % e.g. [marker_data] = btk_loadc3d('c:\data\Session_1\trial001.c3d') will only load the
    % marker data from the C3D file into a structured array called 'marker_data'
    %
    % [marker_data, a_data] = btk_loadc3d() will open a windows dialog box allowing
    % the user to find the file they want to open and load the reconstructed
    % data
    %
    % Author: Behnoosh Parsa (University of Washington)
    % Updated: 11/18/2019
    """
def what_is_in_c3d(c):

    print("# ---- HEADER ---- #")
    print(f"Number of points = {c['header']['points']['size']}")
    print(f"Point frame rate = {c['header']['points']['frame_rate']}")
    print(f"Index of the first point frame = {c['header']['points']['first_frame']}")
    print(f"Index of the last point frame = {c['header']['points']['last_frame']}")
    print("")
    print(f"Number of analogs = {c['header']['analogs']['size']}")
    print(f"Analog frame rate = {c['header']['analogs']['frame_rate']}")
    print(f"Index of the first analog frame = {c['header']['analogs']['first_frame']}")
    print(f"Index of the last analog frame = {c['header']['analogs']['last_frame']}")
    print("")
    print("")
    # Print the parameters
    print("# ---- PARAMETERS ---- #")
    print(f"Number of points = {c['parameters']['POINT']['USED']['value'][0]}")
    print(f"Name of the points = {c['parameters']['POINT']['LABELS']['value']}")
    print(f"Point frame rate = {c['parameters']['POINT']['RATE']['value'][0]}")
    print(f"Number of frames = {c['parameters']['POINT']['FRAMES']['value'][0]}")
    print("")
    print(f"Number of analogs = {c['parameters']['ANALOG']['USED']['value'][0]}")
    print(f"Name of the analogs = {c['parameters']['ANALOG']['LABELS']['value']}")
    print(f"Analog frame rate = {c['parameters']['ANALOG']['RATE']['value'][0]}")
    print("")
    print("")
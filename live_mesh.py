import pyzed.sl as sl

# Create a ZED camera object
zed = sl.Camera()

# Set configuration parameters
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720  # Use HD720 video mode (default fps: 60)
init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP  # Right-handed Y-up
init_params.coordinate_units = sl.UNIT.METER  # Set units in meters

# Open the camera
err = zed.open(init_params)
if err != sl.ERROR_CODE.SUCCESS:
    print("Camera open failed:", err)
    exit(1)

# ✅ Enable positional tracking
tracking_parameters = sl.PositionalTrackingParameters()
err = zed.enable_positional_tracking(tracking_parameters)
if err != sl.ERROR_CODE.SUCCESS:
    print("Positional tracking failed:", err)
    zed.close()
    exit(1)

# ✅ Enable spatial mapping
mapping_parameters = sl.SpatialMappingParameters()
err = zed.enable_spatial_mapping(mapping_parameters)
if err != sl.ERROR_CODE.SUCCESS:
    print("Spatial mapping failed:", err)
    zed.disable_positional_tracking()
    zed.close()
    exit(1)

# Begin grabbing frames
i = 0
py_mesh = sl.Mesh()
runtime_parameters = sl.RuntimeParameters()
while i < 300:
    if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
        mapping_state = zed.get_spatial_mapping_state()
        print("\rImages captured: {0} / 3000 || Mapping State: {1}".format(i, mapping_state), end="")
        i += 1

# Extract full mesh
err = zed.extract_whole_spatial_map(py_mesh)
if err != sl.ERROR_CODE.SUCCESS:
    print("Mesh extraction failed:", err)

# Filter and save mesh
filter_params = sl.MeshFilterParameters()
filter_params.set(sl.MESH_FILTER.LOW)
py_mesh.filter(filter_params)
py_mesh.save("mesh.obj")

# Cleanup
zed.disable_spatial_mapping()
zed.disable_positional_tracking()
zed.close()
print("\n✅ Mesh saved as 'mesh.obj'")


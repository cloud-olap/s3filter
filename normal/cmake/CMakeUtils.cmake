function(showTargetProps target)

    get_target_property(TARGET_INCLUDE_DIRECTORIES ${target} INCLUDE_DIRECTORIES)
    get_target_property(TARGET_INTERFACE_INCLUDE_DIRECTORIES ${target} INTERFACE_INCLUDE_DIRECTORIES)
    get_target_property(TARGET_LINK_LIBRARIES ${target} LINK_LIBRARIES)
    get_target_property(TARGET_LINK_DIRECTORIES ${target} LINK_DIRECTORIES)
    get_target_property(TARGET_INTERFACE_LINK_LIBRARIES ${target} INTERFACE_LINK_LIBRARIES)
    get_target_property(TARGET_INTERFACE_LINK_DIRECTORIES ${target} INTERFACE_LINK_DIRECTORIES)

    message("Target '${target}'  |  Properties:")
    message("  INCLUDE_DIRECTORIES: '${TARGET_INCLUDE_DIRECTORIES}'")
    message("  INTERFACE_INCLUDE_DIRECTORIES: '${TARGET_INTERFACE_INCLUDE_DIRECTORIES}'")
    message("  LINK_LIBRARIES: '${TARGET_LINK_LIBRARIES}'")
    message("  LINK_DIRECTORIES: '${TARGET_LINK_DIRECTORIES}'")
    message("  INTERFACE_LINK_LIBRARIES: '${TARGET_INTERFACE_LINK_LIBRARIES}'")
    message("  INTERFACE_LINK_DIRECTORIES: '${TARGET_INTERFACE_LINK_DIRECTORIES}'")
    message("")

endfunction()

function(setDefaults)

    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fsanitize=undefined")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fsanitize=address")

endfunction()
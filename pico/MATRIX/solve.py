import angr

def main():
    program_path = './matrix'
    project = angr.Project(program_path)
    initiai_state = project.factory.entry_state()
    simgr = project.factory.simgr(initiai_state)
    
    target = 0x5555555551cc
    
    simgr.explore(find=target)

    if simgr.found:
        sol_state = simgr.found[0]
        solution = sol_state.posix.dumps(sys.stdin.fileno())
        print("[+] Solution found! : {}".format(solution.decode('utf-8')))
    else:
        raise Exception("Could not find the solution") #10

# stdin = project.factory.blank_state(addr=0x555555558060)
# 
# input_size = 2
# symbolic_input = angr.claripy.BVV(0x0, input_size * 8)
# 
# stdin.memory.store(0x555555558060, symbolic_input)  
# 
# simgr = project.factory.simulation_manager(stdin)
# simgr.explore()
# 
# if simgr.found:
#     found_state = simgr.found[0]
#     print(f"Found input that reaches the desired path: {found_state.solver.eval(symbolic_input)}")
# else:
#     print("No path found.")

if __name__ == "__main__":
    main()    

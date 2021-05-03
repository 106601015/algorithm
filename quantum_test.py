import math

def find_prime():
    for i in range(9000000, 10000000):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            print(i)

def old_split():
    target = 81000468000451 #9000011 9000041
    for i in range(2, int(math.sqrt(target))+100):
        if target % i == 0:
            print('done:', i, int(target/i))

def quantum_split_test():
    import cirq

    # Pick a qubit.
    qubit = cirq.GridQubit(0, 0)

    # Create a circuit
    circuit = cirq.Circuit(
        cirq.X(qubit)**0.5,  # Square root of NOT.
        cirq.measure(qubit, key='m')  # Measurement.
    )
    print("Circuit:")
    print(circuit)

    # Simulate the circuit several times.
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=20)
    print("Results:")
    print(result)


if __name__ == '__main__':
    print('gogo')
    #find_prime()
    #old_split()
    quantum_split_test()
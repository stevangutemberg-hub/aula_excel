import hashlib
import time
import multiprocessing

TARGET_HASH = "ca6ae33116b93e57b87810a27296fc36"


def check_range(start, end):

    for i in range(start, end):

        candidate = f"{i:09d}"
        hash_value = hashlib.md5(candidate.encode()).hexdigest()

        if hash_value == TARGET_HASH:
            return candidate

    return None


def crack_parallel(num_processes):

    start_time = time.time()

    total = 1000000000
    chunk = total // num_processes

    processes = []
    manager = multiprocessing.Manager()
    result = manager.list()

    def worker(start, end, result):

        for i in range(start, end):

            candidate = f"{i:09d}"
            hash_value = hashlib.md5(candidate.encode()).hexdigest()

            if hash_value == TARGET_HASH:
                result.append(candidate)
                return

    for i in range(num_processes):

        start = i * chunk
        end = (i + 1) * chunk if i != num_processes - 1 else total

        p = multiprocessing.Process(target=worker, args=(start, end, result))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()

    if len(result) > 0:
        print("Senha encontrada:", result[0])
    else:
        print("Senha não encontrada")

    print("Processos:", num_processes)
    print("Tempo de execução:", end_time - start_time, "segundos")

    return end_time - start_time


if __name__ == "__main__":

    for p in [2, 4, 8, 12]:
        crack_parallel(p)
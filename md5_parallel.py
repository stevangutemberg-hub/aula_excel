import hashlib
import time
import multiprocessing

TARGET_HASH = "ca6ae33116b93e57b87810a27296fc36"


def worker(start, end, target_hash, result):
    for i in range(start, end):

        if result.value != -1:
            return

        candidate = f"{i:09d}"
        hash_value = hashlib.md5(candidate.encode()).hexdigest()

        if hash_value == target_hash:
            result.value = i
            return


def crack_parallel(num_processes):

    start_time = time.time()

    total = 1000000000
    chunk = total // num_processes

    processes = []
    result = multiprocessing.Value('i', -1)

    for i in range(num_processes):

        start = i * chunk
        end = (i + 1) * chunk if i != num_processes - 1 else total

        p = multiprocessing.Process(
            target=worker,
            args=(start, end, TARGET_HASH, result)
        )

        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()

    if result.value != -1:
        print("Senha encontrada:", f"{result.value:09d}")
    else:
        print("Senha não encontrada")

    print("Processos:", num_processes)
    print("Tempo:", end_time - start_time, "segundos")


if __name__ == "__main__":

    multiprocessing.freeze_support()  # IMPORTANTE no Windows

    for p in [2, 4, 8, 12]:
        crack_parallel(p)
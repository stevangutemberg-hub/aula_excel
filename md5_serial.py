import hashlib
import time

TARGET_HASH = "ca6ae33116b93e57b87810a27296fc36"

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def crack_serial():

    start_time = time.time()

    for i in range(1000000000):

        candidate = f"{i:09d}"

        if md5_hash(candidate) == TARGET_HASH:
            end_time = time.time()

            print("Senha encontrada:", candidate)
            print("Tempo de execução:", end_time - start_time, "segundos")

            return

    end_time = time.time()

    print("Senha não encontrada")
    print("Tempo de execução:", end_time - start_time, "segundos")


if __name__ == "__main__":
    crack_serial()
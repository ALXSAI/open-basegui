from src.sql_proxy import sql_proxy


def main():
    myproxy = sql_proxy()

    myproxy.close_connection()

if __name__ == "__main__":
    main()


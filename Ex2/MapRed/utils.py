def Emit(key: str, value: str, sep='\t'):
    """
    emmits a key-value pair.
    """
    message = f'{key}'+sep+f'{value}'
    print(message)
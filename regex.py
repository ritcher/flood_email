import re

email = re.compile(r'([a-z0-9]+[_a-z0-9\.-]*[a-z0-9]+)@([a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,4})')

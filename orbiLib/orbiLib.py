from urllib.request import urlopen, Request
import urllib.error
import time
import sys
import random

tombUrl = "https://www.teamorbi.net/tomb/current-version.txt"
cortexUrl = "https://www.teamorbi.net/cortex/current-version.txt"
orbilibUrl = "https://www.teamorbi.net/orbilib/current-version.txt"

PROJECT_URLS = {
    "Tomb": tombUrl,
    "Cortex": cortexUrl,
    "OrbiLib": orbilibUrl,
}

__version__ = "0.1.4"
# Backward compatibility for existing callers.
orbiLib = __version__

def updateCheck(Version, project, *, version_url=None, timeout=5):
    updatePermissions = input = ("Would you like to connect to the Team Orbi servers?\nYour IP may be logged by Cloudflare or Github during this process.\nPress n to cancel update.")
    if updatePermissions != "n":
        url = version_url or PROJECT_URLS.get(project)
        if not url:
            print(f"Unknown project '{project}'. No update URL configured.")
            return None

        try:
            req = Request(
                url,
                headers={"User-Agent": "TeamOrbi-InternetMaster/1.0"}
            )
            with urlopen(req, timeout=timeout) as response:
                file_content = response.read().decode("utf-8").strip()

            if file_content == Version:
                print("Project " + project + " is up to date!")
                return True
            else:
                print(
                    f"Out of date. Your version: {Version}. "
                    f"Latest version: {file_content}."
                )
                return False

        except urllib.error.HTTPError as e:
            print(
                f"Update check unavailable for {project}: HTTP {e.code}. "
                "Please try again later."
            )
            return None

        except urllib.error.URLError as e:
            print(f"Update check unavailable for {project}: {e}")
            return None
    

def type_message(message, delay=0.05):
    """
    Prints a message one character at a time with a delay between each character.
    
    Args:
        message (str): The message to type out
        delay (float): Delay in seconds between each character (default 0.05)
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

tombGreetings = ['Privacy is not for sale, and human rights should not be compromised out of fear or greed. - Pavel Durov', 'Why use a premade tool when I can make a crappy tool myself? - Orbernator']
cortexGreetings = ['The quiz game for that one person with some Buzz Controllers. And that browses GitHub. So just me. - Orbernator']

def greetingMessage(project):
    if project == 'Cortex':
        print(cortexGreetings[random.randint(0,0)])
    elif project == 'Tomb':
        print(tombGreetings[random.randint(0,1)])


def libUpdate():
    return updateCheck(__version__, 'OrbiLib')

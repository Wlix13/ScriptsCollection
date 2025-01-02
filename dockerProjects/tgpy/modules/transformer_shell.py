"""
    name: transformer_shell
    once: false
    origin: tgpy://module/transformer_shell
    priority: 1727734384
"""
def shell(code):
    proc = subprocess.run([os.getenv("SHELL") or "/bin/sh", "-c", code], encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=10)
    return proc.stdout + (f"\n\nReturn code: {proc.returncode}" if proc.returncode != 0 else "")

def sh_trans(cmd):
    if cmd.lower().startswith(".sh "):
        return f"\nshell({repr(cmd[4:])})"
    return cmd

tgpy.api.code_transformers.add("shell", sh_trans)

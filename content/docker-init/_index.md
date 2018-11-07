+++
title = "Docker Init"
outputs = ["Reveal"]
+++

## Init System im Docker Container

{{% figure src="/slides/images/zombie.png" width="25%" %}}

oder "how to reap zombies"

---
{{% section %}}

### Prozesse in Linux
{{% figure src="/slides/images/linux_procs_1.png" width="80%" %}}

---
### Prozess terminiert
{{% figure src="/slides/images/linux_procs_2.png" width="80%" %}}

---
### Warten auf Kindprozess ("Reaping")
{{% figure src="/slides/images/linux_procs_3.png" width="80%" %}}

---
### Prozesse adoptieren
{{% figure src="/slides/images/linux_procs_4.png" width="80%" %}}

{{% /section %}}

---
{{% section %}}

### Docker

* Entrypoint Prozess im Container hat PID 1
* Prozess nimmt "PID 1 Pflichten" nicht wahr

<br/>
**⇾ Folge:** Zombie Prozesse können entstehen

---

### Zombie Prozess
* Prozess ist beendet
* Elternprozess existiert nicht mehr oder führt kein *wait()* aus
* Braucht kaum Ressourcen, aber belegt PID
* */proc/sys/kernel/pid_max* normalerweise 32768

---

### Demo: examples/zombie
```
docker run --rm -ti zombie
docker run --rm -ti --entrypoint dumb-init zombie python3 /root/fork.py
docker run --rm -ti --init zombie python3 /root/fork.py
```

{{% /section %}}

---
{{% section %}}

### Init-Prozess für Container
* [tini](https://github.com/krallin/tini)
* [dumb-init](https://github.com/Yelp/dumb-init)
* [docker --init ...](https://docs.docker.com/engine/reference/run/#specify-an-init-process)
* [s6-overlay](https://github.com/just-containers/s6-overlay)

---

### s6-overlay

* Basiert auf [s6](http://skarnet.org/software/s6/overview.html)
* Stage 1: Prepare
* Stage 2: Execute/Start
  * /etc/fix-attrs.d
  * /etc/cont-init.d
  * Copy & supervise /etc/services.d
* Stage 3: Shutdown stage (SIGTERM, SIGKILL)

{{% /section %}}

---

### tl;dr

Bei langlaufenden Containern, in denen Subprozesse gestartet werden, ist ein dedizierter Init Prozess ein gutes
Pattern.

---
## Quellen
<small>
https://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-problem/
</small>
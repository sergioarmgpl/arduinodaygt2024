# arduinodaygt2024
# Install K3s on RPI 4B
1. Install Raspbian
2. Configure your Network
```
sudo nmcli c mod "Wired connection 1" ipv4.addresses 172.16.0.10/16 ipv4.method manual

sudo nmcli con mod "Wired connection 1" ipv4.gateway 172.16.0.1

sudo nmcli con mod "Wired connection 1" ipv4.dns 172.16.0.1
sudo nmcli -p connection show

/boot/firmware/cmdline.txt
cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory

/etc/sysctl.conf
net.ipv4.ip_forward=1
net.ipv6.conf.all.forwarding=1

sudo apt-get install iptables
```

3. Install K3s
```
MASTER_IP=YOUR_STATIC_IP
curl -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE="644" INSTALL_K3S_EXEC="--disable traefik --tls-san "$MASTER_IP" --node-external-ip="$MASTER_IP" --node-ip="$MASTER_IP" --disable=servicelb" sh -s -
```
4. Compile containers
docker context use desktop-linux
https://github.com/abiosoft/colima/issues/52


# Installing MetalLB
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.4/config/manifests/metallb-native.yaml

cat <<EOF | kubectl create -f -
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: first-pool
  namespace: metallb-system
spec:
  addresses:
  - 192.168.1.240-192.168.1.250
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: example
  namespace: metallb-system
EOF

# Deploy the YAML files
```
kubectl apply -f yaml
```

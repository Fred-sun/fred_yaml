FROM ubuntu:20.04
MAINTAINER Fred<xiuxi.sun@qq.com>
# Cop ansible depend packages
COPY requirements-azure.txt /usr/local/requirements-azure.txt

# Set Working path
ENV MYPATH /usr/local
WORKDIR $MYPATH

# set ENV variable
ENV AZURE_SUBSCRIPTION_ID=xxxxxxx
ENV AZURE_CLIENT_ID=xxxxxxxx
ENV AZURE_SECRET=xxxxxxxx
ENV AZURE_TENANT=xxxxxxxx

# Update  source
RUN apt-get update -y
# Install depend packages
RUN apt-get install python3-pip wget npm git
RUN pip3 install ansible[azure]
RUN ansible-galaxy collection install azure.azcollection
RUN npm install -g n
RUN n stable
RUN npm install -g autorest
RUN npm install -g typescript
RUN git clone https://github.com/Azure/azure-rest-api-specs.git
RUN git clone https://github.com/haiyuazhang/autorest.ansible.git
RUN cd autorest
RUN npm install 

EXPOSE 8080

def main():
    from twisted.application import internet
    from twisted.application import service
    from keepmail import KeepmailSMTPFactory
    
    application = service.Application("Keepmail Dummy SMTP Server")
    internet.TCPServer(2500, KeepmailSMTPFactory()).setServiceParent(application)

    return application

application = main()

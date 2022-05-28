class llIIllIIllIIlllI:
    def __init__(IIlIlIllIIlll, IllIIllIIIlIII):
        IIlIlIllIIlll.lIIIlllIlIl = IllIIllIIIlIII
        IIlIlIllIIlll.lIllIllIlI = 0
        IIlIlIllIIlll.IlIIllllllIlI()
    def IlIIllllllIlI(IIlIlIllIIlll):
        IlIlIIIIlllIlll = [-1] * IIlIlIllIIlll.lIIIlllIlIl
        IIlIlIllIIlll.IlIIllIIIlI(IlIlIIIIlllIlll, 0)
        print("Found", IIlIlIllIIlll.lIllIllIlI, "solutions.")
    def IlIIllIIIlI(IIlIlIllIIlll, IlIlIIIIlllIlll, llIIIIIIII):
        if llIIIIIIII == IIlIlIllIIlll.lIIIlllIlIl:
            IIlIlIllIIlll.llIlIllIllIlllIIlIll(IlIlIIIIlllIlll)
            IIlIlIllIIlll.lIllIllIlI += 1
        else:
            for llIlIIlllIlIIlIIl in range(IIlIlIllIIlll.lIIIlllIlIl):
                if IIlIlIllIIlll.IIIIIlIlIIII(IlIlIIIIlllIlll, llIIIIIIII, llIlIIlllIlIIlIIl):
                    IlIlIIIIlllIlll[llIIIIIIII] = llIlIIlllIlIIlIIl
                    IIlIlIllIIlll.IlIIllIIIlI(IlIlIIIIlllIlll, llIIIIIIII + 1)
    def IIIIIlIlIIII(IIlIlIllIIlll, IlIlIIIIlllIlll, IIllIlIllI, llIlIIlllIlIIlIIl):
        for IIIIlIlllIllIIIlIll in range(IIllIlIllI):
            if IlIlIIIIlllIlll[IIIIlIlllIllIIIlIll] == llIlIIlllIlIIlIIl or IlIlIIIIlllIlll[IIIIlIlllIllIIIlIll] - IIIIlIlllIllIIIlIll == llIlIIlllIlIIlIIl - IIllIlIllI or IlIlIIIIlllIlll[IIIIlIlllIllIIIlIll] + IIIIlIlllIllIIIlIll == llIlIIlllIlIIlIIl + IIllIlIllI:
                return False
        return True
    def llIlIllIllIlllIIlIll(IIlIlIllIIlll, IlIlIIIIlllIlll):
        for IIIIIlIlIIllII in range(IIlIlIllIIlll.lIIIlllIlIl):
            IIlIIIIlIIIlllIlI = ""
            for llIlIIlllIlIIlIIl in range(IIlIlIllIIlll.lIIIlllIlIl):
                if IlIlIIIIlllIlll[IIIIIlIlIIllII] == llIlIIlllIlIIlIIl:
                    IIlIIIIlIIIlllIlI += "Q "
                else:
                    IIlIIIIlIIIlllIlI += ". "
            print(IIlIIIIlIIIlllIlI)
        print("\n")
    def llIlIIlIIllIll(IIlIlIllIIlll, IlIlIIIIlllIlll):
        IIlIIIIlIIIlllIlI = ""
        for IIIIlIlllIllIIIlIll in range(IIlIlIllIIlll.lIIIlllIlIl):
            IIlIIIIlIIIlllIlI += str(IlIlIIIIlllIlll[IIIIlIlllIllIIIlIll]) + " "
        print(IIlIIIIlIIIlllIlI)
def lIIIllIlIIIIlIIIlll():
    llIIllIIllIIlllI(8)
if __name__ == "__main__":
    lIIIllIlIIIIlIIIlll()
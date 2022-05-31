class IIIIIlIlIlllIl:
    def __init__(IIllIIIIIlllI, lllllIIIlllllIIIIIIl):
        IIllIIIIIlllI.llIIlIIlIIIII = lllllIIIlllllIIIIIIl
        IIllIIIIIlllI.llIlIIlIIIIlIlI = 0
        IIllIIIIIlllI.IlIllIIIIlIIl()
    def IlIllIIIIlIIl(IIllIIIIIlllI):
        IIIIIlIIIlIIIl = [-1] * IIllIIIIIlllI.llIIlIIlIIIII
        IIllIIIIIlllI.IIIIIIlIlIlIlIlIIII(IIIIIlIIIlIIIl, 0)
        print("Found", IIllIIIIIlllI.llIlIIlIIIIlIlI, "solutions.")
    def IIIIIIlIlIlIlIlIIII(IIllIIIIIlllI, IIIIIlIIIlIIIl, llIIIllIlIII):
        if llIIIllIlIII == IIllIIIIIlllI.llIIlIIlIIIII:
            IIllIIIIIlllI.lIlllIllIIl(IIIIIlIIIlIIIl)
            IIllIIIIIlllI.llIlIIlIIIIlIlI += 1
        else:
            for lIlIIllIIlIIllIII in range(IIllIIIIIlllI.llIIlIIlIIIII):
                if IIllIIIIIlllI.IlIlIlIIlIIIlI(IIIIIlIIIlIIIl, llIIIllIlIII, lIlIIllIIlIIllIII):
                    IIIIIlIIIlIIIl[llIIIllIlIII] = lIlIIllIIlIIllIII
                    IIllIIIIIlllI.IIIIIIlIlIlIlIlIIII(IIIIIlIIIlIIIl, llIIIllIlIII + 1)
    def IlIlIlIIlIIIlI(IIllIIIIIlllI, IIIIIlIIIlIIIl, IIIllIIlIlI, lIlIIllIIlIIllIII):
        for llIlIIIIIl in range(IIIllIIlIlI):
            if IIIIIlIIIlIIIl[llIlIIIIIl] == lIlIIllIIlIIllIII or                IIIIIlIIIlIIIl[llIlIIIIIl] - llIlIIIIIl == lIlIIllIIlIIllIII - IIIllIIlIlI or                IIIIIlIIIlIIIl[llIlIIIIIl] + llIlIIIIIl == lIlIIllIIlIIllIII + IIIllIIlIlI:
                return False
        return True
    def lIlllIllIIl(IIllIIIIIlllI, IIIIIlIIIlIIIl):
        for lIIIIlllIlIIIIIllI in range(IIllIIIIIlllI.llIIlIIlIIIII):
            lIIllllIIIllIII = ""
            for lIlIIllIIlIIllIII in range(IIllIIIIIlllI.llIIlIIlIIIII):
                if IIIIIlIIIlIIIl[lIIIIlllIlIIIIIllI] == lIlIIllIIlIIllIII:
                    lIIllllIIIllIII += "Q "
                else:
                    lIIllllIIIllIII += ". "
            print(lIIllllIIIllIII)
        print("\n")
    def lIIIllllIIlIIlIlllII(IIllIIIIIlllI, IIIIIlIIIlIIIl):
        lIIllllIIIllIII = ""
        for llIlIIIIIl in range(IIllIIIIIlllI.llIIlIIlIIIII):
            lIIllllIIIllIII += str(IIIIIlIIIlIIIl[llIlIIIIIl]) + " "
        print(lIIllllIIIllIII)
def lIIIllIlllllIll():
    IIIIIlIlIlllIl(8)
if __name__ == "__main__":
    lIIIllIlllllIll()
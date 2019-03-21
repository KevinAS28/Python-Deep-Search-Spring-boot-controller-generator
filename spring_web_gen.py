import sys
import os

template = """
@GetMapping("%s")
public String %s(Model M)
{
    return "%s";
}
"""
#i = "dataNasabah"
#print(template%("/"+i.lower(), i, i.lower()))
#sys.exit(0)
l0 = {
    "cif":{
        "pemeriksaanDataNasabah":{},
        "pemeriksaanDataDaftarHitam":{},
        "cifExpress":{},
        "cifPerorangan":{},
        "cifBadanHukum":{
            "pemeliharanCifBadanHukum":{},
            "uploadDataLaporanKeuanganDebitur":{},
            "LaporanKeuanganDebitur":{}
        },
        
        "tandaTangan":{},
        "perubahanDataSandiLokasiDanDati2":{},
        "pemeliharanNoDin":{},
        "hapusDataCifYangTidakPunyaRekening":{},
        "pemeliharanPengaduanNasabah":{},
        "logOffLogIn":{},
        "exit":{}
    },
    
    "customer":{
        "tabungan":{
            "pesanNoTabungan":{},
            "dataMaster":{},
            "pembuatanDataMasterTabunganViaExcell":{},
            "cetakID":{},
            "cetakMutasiTanpaBuku":{},
            "lihatProofCodeTabungan":{},
            "otoritasiTabunganPasif":{},
            "penutupanTabunganManual":{
                "penutupanTabunganManual":{
                    "penutupanSatuRekening":{},
                    "penutupanBanyakRekening":{}
                    }
            },
            "bilyetTabunganBerjangka":{
                "generateBuktiSetoran":{},
                "cetakBuktiSetoran":{}
            },            
            "perhitunganPoint":{},
            "cardManagement":{
                "generateKartu":{},
                "lirikKartuDenganTabungan":{},
                "generatePin":{},
                "pembuatanPinBaruOlehNasabah":{},
                "pembuatanPinOlehNasabah":{},
                "resetPin":{}
            },
            "informasiDataPenggesekanKartuSergu":{},
            "pembentukanDataKelompok":{
                "dataNasabahKelompok":{},
                "dataRekeningNasabahKelompok":{},
                "pembentukanTopSheetHarian":{},
                "hapusTopSheetHarian":{},
                "pembentukanDataDropping":{}
            }
        },
        "deposito":{
                "bilyet":{},
                "masterDeposito":{},
                "masterDepositoBlackDate":{},
                "perpanjanganDepositoManual":{},
                "cetakBilyetPercobaan":{},
                "cetakBilyet":{},
                "registrasiBilyetRusakHilang":{},
                "perubahanNisbahTemporary":{},
                "pembatalanBilyetYangBelumDicetak":{},
                "perubahanIndikasiRateSyariah (IRS)":{},
                "uploadPerubahanIdikasiRateSyariah (IRS)":{}
            },
        "pemeliharanMerchant":{},
        "perubahanNoCif":{},
        "perubahanProdukCustomer":{},
        "perubahanProdukCustomer (Upload File Excel)":{},
        "perubahanStatusZakat":{},
        "blokir":{},
        "releaseBlokir":{},
        "releaseBlokirMassal":{},
        "kondisiKhusus":{},
        "release":{},
        "releaseKondisiKhusus":{},
        "standingInstruction":{},
        "daftarHitam":{},
        "slipKolektor":{},
        "perubahanAoMassal":{},
        "uploadKodeMarketingViaExcell":{},
        "virtualAccount":{
            "uploadDataVirtualAccountDariExcell":{},
            "otoritasDataUpload":{},
            },
        "eChannel":{
            "pemeliharaanDataPesertaSms":{},
            "uploadDataPesertaSms":{}
        },
        "uploadDataPesertaDidik":{},
        "pemeliharaanDataPesertaDidik":{},
        "pembentukanDataPesertaDidik":{},
        "perubahanKodeKolektor":{}
    },
    "persediaanAsset":{
        "masterAsset":{},
        "releaseNoKontrakPadaMasterAset":{},
        "perubahanKelompokPersediaan":{},
        "ijarah":{
            "linkNoKontrak":{},
            "unlinkNoKontrak":{}
        }
    },
    "jaminan":{
        "masterJaminan":{},
        "overideJaminanTidakCukup":{},
        "peminjamanAgunan":{},
        "pengembalianAgunan":{},
        "pertukaranAgunan":{},
        "pengembalianAgunan":{},
        "ayda":{},
        "masterAsuransi":{},
        "masterAsuransiUpload":{}
    },
    "treasury":{
        "dataCasie": {
            "registrasiDataCassie":{},
            "otorasiDataCassie":{},
            "releaseDataCassie":{}
        },
        "pembiayaanDariBankNonBank":{},
        "jadwalAngsuranHutang":{},
        "transaksiTreasury":{
            "transaksiPencairan":{},
            "transaksiAngsuran":{},
            "transaksiPelunasan":{},
        }
    },
    "penyaluran":{
        "masterFile":{
            "fasilitasWaad":{},
            "mudharabah":{},
            "mudharabahTerikat":{},
            "musyarakah":{},
            "murabahah":{},
            "qardh":{},
            "qardhHasan":{},
            "ijarah":{},
            "ijarahMuntahiyahBittamlik":{},
            "putangMutijasa":{},
            "salam":{},
            "istishna":{},
            "hawalah":{},
            "rahn":{}
            },
        "perpanjanganPembiayaan (Non Restrukuturisasi)":{},
        "perubahanStatusMaster":{},
        "uploadMasterFileViaExcell":{},
        "releaseHoldJaminan":{},
        "jadwalPembayaran":{
            "standard":{},
            "ballonPayment":{},
            "proyeksiPendapatan":{},
            "cetakJadwalPembayaran":{},
            "recoveryJadwalPembayaran":{},
            "perubahanTanggalAngsuran":{},
            "perubahanTagihan":{},
            "penggabunganJadwalPembayaran":{},
            "koneksiTransaksiPPMusyarakahMudharabah":{}
        },
        "cetakDokumen":{
            "kuitansi":{},
            "kuitansiUlang":{},
            "generateKuitansiTagihan":{},
            "cetakKuitansiTagihan":{},
            "cetakTandaTerimaAngsuran":{},
            "cetakRekapitulasiKuitansiTagihan":{},
            "cetakRekapitulasiKuitansiTagihanPensiunan":{},
            "pembuatanDaftarTabunganPickUpHarian":{},
            "uploadDaftarSetoranPerGroupDebitur":{},
            "otorasasiDaftarSetoranPerGroupDebitur":{},
            "transaksiDaftarSetoranPerGroupDebitur":{}
        },
        "simulasiPembiyaan":{},
        "perbandinganRepaymentSchedule":{},
        "perubahanColl":{},
        "mantaincePenyebabMacet":{},
        "perubahanJadwalDropingBertahap":{},
        "perubahanPendebetanOtomatis":{},
        "pemeliharaanDenda":{
            "perubahanPengenaanDenda":{},
            "perubahanNominalDenda":{}
        },
        "pemeliharaanBagiHasil":{
            "perubahanProyeksiBagiHasil":{},
            "perubahanSisaProyeksiBagiHasil":{}
        },
        "linkAgunan":{},
        "unLinkAgunan":{},
        "Restrukuturisasi":{
            "reScheduling":{},
            "reConditioning":{},
            "reStructuring":{}
        },
        "plafondIndukGroupDebitur":{},
        "uploadDataAmortisasiByAdminViaExcell":{},
        "hapusDataAmortisasiByAdmViaExell":{},
        "hapusDataPendDanBiayaEtapYgSudahLunas":{},
        "hapusDataPendDanBiayaEtapYgBelumDiproses":{},
        "perubahanSandiBiPembiayaanJatuhTempo":{},
        "perubahanSandiSlikMasterPembiayaan":{},
        "updateDanUploadKodeAtmrPembiayaan":{}
        },
    "transaksiUmum":{
        "umum":{},
        "umumMulti":{},
        "postingGajiSDM":{},
        "transaksiMassalKolektor":{},
        "otorisasiTransaksi":{},
        "reverseTransaksi":{},
        "transaksiBackDated":{},
        "transaksiFuture":{},
        "transaksiPencairanTitipanWarkatKliring":{},
        "transaksiPengirimanUangKeKantorPusatCabang":{},
        "transaksiPenerimaanUangDarKantorPusatCabang":{},
        "pencairanTagihanPihakKetiga":{},
        "uploadDataTransaksiViaExcell":{},
        "uploadDataTransaksiVABankPermataManual":{},
        "uploadDataTransaksiVACimbNiagaManual":{},
        "mutasiLokasiCustomer":{},
        "penutupanLokasiKantor":{},
        "penutupanTabunganKeTabunganViaExcell":{},
        "transaksiKelompok":{}
    },
    "transaksiKhusus":{
        "titipan":{
            "pencairanTitipan":{}
        },
        "asset":{
            "pembelianAsset":{},
            "penyusutan":{},
            "penyusutanIjarahImbtAngsuran":{},
            "penyusutanBaseSchedule":{},
            "penyusutanSekaligus":{},
            "perbaikan":{},
            "penjualan":{},
            "pengalihanAgunanKeAyda":{},
            "penjualanAyda":{},
            "penjualanAydaSebagian":{},
        },
        "tabunganVa":{
            "bonusTabungan":{},
            "bonusTabunganDiprosesAwalBulan":{},
            "pencairanTaxDiprosesAwalBulan":{},
            "penutupanVa":{}
        },
        "deposito":{
            "pembukaan":{},
            "pembukaanBagiHasilDepositoManual":{},
            "pembukuanBagiHasilDepositoDipercepat":{},
            "pembukuanBddBagiHasil":{},
            "pembukuanResiBagiHasilDeposito":{},
            "pembukuanTitipanBaghasDeposito":{},
            "pencairanTaxDeposito":{},
            "pencairanBaghasDiTranserPadaBankLain":{},
            "pencairanDeposito":{},
            "cetakResiPencairanDeposito":{}
        },
        "waad":{
            "pembukaanWaad":{},
            "penutupanWaad":{},
        },
        "mudharabah":{
            "droppingMudharabah":{},
            "modalBagiHasilMenggunakanPP":{},
            "bagiHasil":{},
            "bagiHasilYangAkanDiterima":{},
            "AngsuranModalMudharabah":{},
            "pelunasanModal":{}
        },
        "musyarakah":{
            "droppingMusyarakah":{},
            "modalBagiHasilMenggunakanPP":{},
            "bagiHasil":{},
            "bagiHasilYangAkanDiterima":{},
            "AngsuranModalMusyarakah":{},
            "pelunasanMusyarakah":{}
        },        
        "hawalah":{
            "droping":{},
            "angsuran":{},
            "pelunasan":{}
        },
        "rahn":{
            "droping":{},
            "angsuran":{},
            "pelunasan":{}
        },
        "murabahah":{
            "penerimaanUangMuka":{},
            "droping":{},
            "angsuran":{},
            "penurunanBakiDebet":{},
            "pelusananDipercepat":{},
            "koreksiMarginAwal":{},
            "discountMarginBerjalan":{}
        },
        "salam":{
            "dropping":{},
            "penerimaanBarangPesanan":{},
            "pembatalanPesanan":{},
            "penjualanJaminan":{},
            "angsuranSalam":{},
            "pelunasanSalam":{}
        },
        "istishna":{
            "dropingIstishna":{},
            "angsuranIstihna":{},
            "penurunanBakiDebetIstishna":{},
            "pelunasanIstishna":{},
            "penyerahanPesanan":{},
            "pembatalanPesanan":{},
            "pembayaranIstishna":{}
        },
        "ijarahImbt":{
            "dropingIjarah":{},
            "penerimaanUangSewaDimuka":{},
            "penerimaanUangSewa":{},
            "pelunasanIjarahImbt":{},
            "hibah":{}
        },
        "ijarahMultiJasa":{
            "droping":{},
            "angsuran":{},
            "penurunanBakiDebetPm":{},
            "pelunasan":{}
        },
        "qardh":{
            "droping":{},
            "angsuran":{},
            "pelunasan":{}            
        },
        "denda":{},
        "dendaSesuaiJadwalAngsuran":{},
        "reverseAcrual":{},
        "reverseAcrualBaseOnTransaksi":{},
        "prosesAcrual":{},
        "transaksiMassal":{
            "dropingMassalViaUploadExcel":{},
            "angsuranMassal":{},
            "angsuranMassalChanneling":{},
            "angsuranMassalPerlokasi":{},
            "angsuranMassalViaTeller":{},
            "angsuranKolektifViaDaftarTagihan":{},
        },
        "restrukturisasi":{},
        "WoWriteOff":{
            "wo":{},
            "woMassalByUploadExcel":{},
            "angsuranWo":{},
            "hapusTagih":{}
        },
        "biayaProses":{},
        "koreksiTransaksiLalu":{},
        "koreksiKelebihanBayar":{},
        "biayaAdminEtap":{
            "pencairanByAdministrasiYangBelumDiproses":{},
            "pembatalanAnnortisasiByAdministrasi":{},
            "penihilanSaldoByAdministrasiYangMinus":{}
        },
        "pembukaanPpap":{},
        "cassie":{
            "penerimaanDanaDariBankNonBank":{}
        }
    },
    "laporan":{
        "transaksi":{
            "jurnalTransaksiPerBatch":{},
            "jurnalTransaksiPerKantor":{},
            "jurnalTransaksiSeluruhKantor":{},
            "jurnalTransaksiPosAdm":{},
            "rekapitulasiTransaksi":{},
            "verfikasiSbbPeralihan":{},
            "verifikasiTglTransaksi":{},
            "transaksiEdc":{},
            "monitoringSetoranTabunganWajib":{}
        },
        "transaksiTitipanSetoranAngsuran":{},
        "transaksiPembiayaan":{},
        "transaksiPerAo":{},
        "transaksiAntarKantor":{},
        "transaksiAtm":{},
        "controlBatchTransaksi":{},
        "transaksiKolektifGroupDebitur":{},
        "neracaDnLabaRugiPercobaan":{},
        "fasilitasNasabah":{},
        "oneObligor":{},
        "infromasiCif":{},
        "informasiPoint":{},
        "customerBirthday":{},
        "rateKonverter":{},
        "informasiMutasiKasDanBankHariIni":{},
        "informasiMutasiBankHariIni":{},
        "informasiLR":{},
        "infromasiSaldoViaPhone":{},
        "riwayatTransaksiRekening":{},
        "informasiDebitur":{},
        "daftarTitipanWarkatKliring":{},
        "tabunganBermutasi":{},
        "distribusiBaghasDeposito":{},
        "daftarRealisasiResiBagiHasil":{},
        "Sppd":{},
        "daftarPembukaanProdukHariIni":{},
        "laporanUntukMitraKerja":{
            "riwayatSetoranSumbanganPendidikan":{},
            "laporanSetoranHarian":{}
        }
    },
    "tools":{
        "printSetup":{},
        "perubahanPassword":{},
        "releaseUser":{},
        "updateSbbMaster":{},
        "updateCounterProduk":{},
        "updateSbbPeralihan":{},
        "pembentukanSaldoHarianTabungan":{},        
        "recoverySaldoHrianTabungan":{},
        "recoverySaldoHrianTabunganViaUploadExcell":{},
        "recoveryByAdministrasiAmortasi":{},
        "recoverySaldoHarianTabungan":{},
        "updateRatePembiayaan":{},
        "rekonsiliasiTransaksiTabungan":{},
        "toolbars":{},
        "freeMemory":{},
        "pcInfo":{},
        "regionalSettingInfo":{},
        "logAktivitasUser":{},
        "updateSaldoRate2Produk":{},
        "uploadKodeGroupDebitur":{},
        "uploadKodeGroupDiCif":{},
        "uploadDataGroupDebitur":{},
        "uploadDataGroupDanaPembiayaan":{},
        "uploadDataKolektor":{},
        "updateKodeProdukTabungan":{},
        "perbaikanDataSlik":{
            "dataGolonganNasabah":{},
            "dataPekerjaan":{},
            "dataPenjamin":{}
        },
        "updateTabunganDiMasterPembiayaan":{},
        "updateSaldoTabungan":{},
        "perbaikanDataPendAdmPembiayaan":{}
    },
    "help":{},
    "exit":{}
}


#cara 1 copy nanti rm 1 1



index= [0]
obj = ""

def dictAccess(kamus, daftar):
    addr = ""
    for i in daftar:
        keys = list(kamus.keys())
        key = keys[i]
        #print("kunci: %s"%(key))
        kamus = kamus[key]
    return kamus
def addrDictAccess(kamus, daftar):
    addr = ""
    for i in daftar:
        keys = list(kamus.keys())
        key = keys[i]
        addr=os.path.join(addr, key)
        kamus = kamus[key]
    return addr

l1 = l0.copy()
dalam = []
dal = []
i = 0
mundur = 0
obj = ""
cuk = 0

def onFinish():
    lengkap = """
					<!-- Menu CIF  -->
				<li class="nav-item dropdown">


					<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown"
					 aria-haspopup="true" aria-expanded="false">
						CIF
					</a>
					<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
						<a class="dropdown-item" href="/page=pemdana">Pemeriksaan Data Nasabah</a>
						<!-- Drop Right Submenu -->
						<div class="dropdown-submenu">
							<a class="dropdown-item dropdown-toggle" href="#" id="DropdownMenuLink" role="button" data-toggle="dropdown"
							 aria-haspopup="true" aria-expanded="false">
								CF Bandingan
                                                        </a>
                                                            <div class="dropdown-menu rightdrop" id="" aria-labelledby="DropdownMenuLink">
                                                                    <a class="dropdown-item" href="#">A</a>
                                                                    <a class="dropdown-item" href="#">B</a>
                                                                    <a class="dropdown-item" href="#">B</a>
                                                                    <a class="dropdown-item" href="#">B</a>
                                                            </div>
						</div>
						<!-- End Drop Right  -->
					</div>
				</li>
                                """
    cif_saja = """
					<!-- Menu CIF  -->
				<li class="nav-item dropdown">


					<a class="nav-link dropdown-toggle" href="%s" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown"
					 aria-haspopup="true" aria-expanded="false">
						%s
					</a>
					
				</li>    
    """
    isi_cif = """
					<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
						<a class="dropdown-item" href="/page=pemdana ">Pemeriksaan Data Nasabah</a>
					</div>
    """
    cif_dropdown = """

						<div class="dropdown-submenu">
							<a class="dropdown-item dropdown-toggle" href="#" id="DropdownMenuLink" role="button" data-toggle="dropdown"
							 aria-haspopup="true" aria-expanded="false">
								CF Bandingan
                                                        </a>

						</div>
    """
    isi_cif_dropdown = """
                                                            <div class="dropdown-menu rightdrop" id="" aria-labelledby="DropdownMenuLink">
                                                                    <a class="dropdown-item" href="#">A</a>
                                                                    <a class="dropdown-item" href="#">B</a>
                                                                    <a class="dropdown-item" href="#">B</a>
                                                                    <a class="dropdown-item" href="#">B</a>
                                                            </div>    
    """
    template = """

    """
    with open("RoutingController.java", "r") as baca:
        baca = baca.read()
        for i in dalam:
            
            
            #i = addrDictAccess(l0, i)
            #if (i==""):
                #continue            
            ##cek apakah cuma 1 dir, karena dir pertama hannya kategori
            #cek = os.path.split(i)
            #if(cek[0]==""):
                #continue
            
            #a = os.path.join("api_object", i)
            #try:
                #os.makedirs(a)
            #except:
                #pass
            
            #cn = list(os.path.basename(i))
            #cn[0] = cn[0].upper()
            #classname = ""
            #for b in cn:
                #classname+=b
            
            #towrite = baca%(classname, os.path.basename(i))
            #with open(a+"Obj.java", "w+") as tulis:
                #tulis.write(towrite)
            
            
    return True

while True:
    try:
        obj = dictAccess(l0, dal)
        dal.append(i)   
    except IndexError:
        #mundur 1
        dal = dal[:-1]
        dalam.append(dal)
        if (len(dal)==0):            
            for i in range(len(dalam)):
                dalam[i] = dalam[i][:-1]
            onFinish()
            break
        dal[-1]+=1
        

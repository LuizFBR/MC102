aux = 0
lucro = 0
lucro_aux = 0
um_lucro = False

for z in range:
    for x in range:
        for c in range:
            for v in range:
                for b in range:
                    for n in range:
                        for j in range:

                            for i in range:
                                aux = i
                                i_emp1 = list_emp1.index(i)

                                if um_lucro is True and lucro_aux > lucro:
                                    lucro = lucro_aux
                                    um_lucro = False

                                if lucro > aux:
                                    lucro = i - aux
                                    lucro_aux = lucro
                                    um_lucro = True
                                else:
                                    aux = i
                                if aux == 0 and lucro == 0:
                                    i_Cemp1 = i_emp1

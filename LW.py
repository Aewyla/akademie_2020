#LW AH values
penumbra = 7.20
print('Penumbra Thread in SW for 7.20 g.')
leather = float(input('Price Desolate leather for one: '))
bone = float(input('Price Pallid bone for one: '))
#shadowlands recipes

lw_recipes = dict(des_sc_pauldrons=(36.0569 - (penumbra * 3 + leather * 7 + bone * 2)),
                  des_sc_greaves=(51.7307 - (penumbra * 4 + leather * 9 + bone * 3)),
                  des_sc_helm=(38.9805 - (penumbra * 2 + leather * 6 + bone * 3)),
                  des_sc_vest=(52.3040 - (penumbra * 4 + leather * 9 + bone * 3)),
                  des_sc_gauntlets=(26.0951 - (penumbra * 1 + leather * 6 + bone * 2)),
                  des_sc_waistguard=(23.7117 - (penumbra * 2 + leather * 3 + bone * 2)),
                  des_sc_armguards=(23.8213 - (penumbra * 1 + leather * 4 + bone * 2)),
                  des_sc_treads=(38.3501 - (penumbra * 2 + leather * 6 + bone * 2)),
                  des_le_pauldrons=(38.7364 - (penumbra * 3 + leather * 10)),
                  des_le_greaves=(50.2792 - (penumbra * 4 + leather * 12)),
                  des_le_vest=(49.4739 - (penumbra * 4 + leather * 12)),
                  des_le_helm=(37.8866 - (penumbra * 2 + leather * 10)),
                  des_le_gauntlets=(25.3577 - (penumbra * 1 + leather * 9)),
                  des_le_waistguard=(25.4670 - (penumbra * 2 + leather * 5)),
                  des_le_armguards=(25.5780 - (penumbra * 1 + leather * 6)),
                  des_le_treads=(36.2825 - (penumbra * 2 + leather * 9)),
                  compo_cross=(89.8607 - (penumbra * 10 + leather * 5 + bone * 2)),
                  b_b_knuc=(71.3733 - (penumbra * 5 + leather * 8 + bone * 6)),
                  compo_bow=(89.5431 - (penumbra * 8 + leather * 5 + bone * 6)),
                  d_l_cest=(71.1121 - (penumbra * 5 + leather * 10 + bone * 4)))


for key, value in lw_recipes.items():
    print(key, ' : ', value)

print(max(lw_recipes, key=lw_recipes.get))
print(min(lw_recipes, key=lw_recipes.get))
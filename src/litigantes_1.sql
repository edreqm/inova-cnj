select distinct *
from
(
select nr_processo, nr_doc_principal_pessoa, nm_pessoa, cd_orgao, nm_orgao, cd_municipio_ibge, sg_tribunal
from tb_processo
where ds_grau_orgao = 'G1'
and tp_polo = 'PA'
union all
select nr_processo, nr_doc_principal_pessoa, nm_pessoa, cd_orgao, nm_orgao, cd_municipio_ibge, sg_tribunal
from tb_processo
where ds_grau_orgao = 'G2'
and tp_polo = 'PA'
and nr_processo like '%0000'
union all
select nr_processo, nr_doc_principal_pessoa, nm_pessoa, cd_orgao, nm_orgao, cd_municipio_ibge, sg_tribunal
from tb_processo
where ds_grau_orgao = 'G2'
and tp_polo = 'AT'
and nr_processo not like '%0000'
) x

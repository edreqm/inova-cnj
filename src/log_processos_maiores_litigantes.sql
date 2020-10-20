-- Inspeção de tempo de duração dos processos
select max(dias_duracao_processo)
from (
	-- k processos com menor duracao
	select 
		nr_processo, dias_duracao_processo
	from 
		minerador_processos.mv_maiores_litigantes_arquivados
	where 
		-- Ajuste aqui o identificador do litigante
		-- nr_doc_principal_pessoa ilike '00360305%' and
	
		-- Ajuste aqui a classe processual
		nr_classe_processual = 985
	group by 
		nr_processo, dias_duracao_processo
	order by dias_duracao_processo asc
	-- Ajuste aqui o numero de processos a sererm considerados
	limit 100
) x;


-- Geração do log dos processos para mineração
select 
	ml.nr_processo, 
	ml.dt_lancamento_movimento, 
	ml.ds_movimento_complementos
from 
	minerador_processos.mv_maiores_litigantes_arquivados ml
	join (
		-- k processos com menor duracao
		select 
			ml2.nr_processo, 
			ml2.dias_duracao_processo
		from 
			minerador_processos.mv_maiores_litigantes_arquivados ml2
		where 
			-- Ajuste aqui o identificador do litigante
			-- nr_doc_principal_pessoa ilike '00360305%' and

			-- Ajuste aqui a classe processual
			ml2.nr_classe_processual = 985
		group by 
			ml2.nr_processo, 
			ml2.dias_duracao_processo
		order by ml2.dias_duracao_processo asc
		-- Ajuste aqui o numero de processos a sererm considerados
		limit 100
	) melhores on melhores.nr_processo = ml.nr_processo
group by ml.nr_processo, ml.dt_lancamento_movimento, ml.ds_movimento_complementos
order by ml.nr_processo, ml.dt_lancamento_movimento;
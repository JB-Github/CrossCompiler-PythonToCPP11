// Generated from py.g4 by ANTLR 4.2
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link pyParser}.
 */
public interface pyListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link pyParser#else_}.
	 * @param ctx the parse tree
	 */
	void enterElse_(@NotNull pyParser.Else_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#else_}.
	 * @param ctx the parse tree
	 */
	void exitElse_(@NotNull pyParser.Else_Context ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#for_}.
	 * @param ctx the parse tree
	 */
	void enterFor_(@NotNull pyParser.For_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#for_}.
	 * @param ctx the parse tree
	 */
	void exitFor_(@NotNull pyParser.For_Context ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#mod_alias}.
	 * @param ctx the parse tree
	 */
	void enterMod_alias(@NotNull pyParser.Mod_aliasContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#mod_alias}.
	 * @param ctx the parse tree
	 */
	void exitMod_alias(@NotNull pyParser.Mod_aliasContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#gen_expr}.
	 * @param ctx the parse tree
	 */
	void enterGen_expr(@NotNull pyParser.Gen_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#gen_expr}.
	 * @param ctx the parse tree
	 */
	void exitGen_expr(@NotNull pyParser.Gen_exprContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#pos_paramtuple}.
	 * @param ctx the parse tree
	 */
	void enterPos_paramtuple(@NotNull pyParser.Pos_paramtupleContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#pos_paramtuple}.
	 * @param ctx the parse tree
	 */
	void exitPos_paramtuple(@NotNull pyParser.Pos_paramtupleContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(@NotNull pyParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(@NotNull pyParser.NumberContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#lambda}.
	 * @param ctx the parse tree
	 */
	void enterLambda(@NotNull pyParser.LambdaContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#lambda}.
	 * @param ctx the parse tree
	 */
	void exitLambda(@NotNull pyParser.LambdaContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#block_stmt}.
	 * @param ctx the parse tree
	 */
	void enterBlock_stmt(@NotNull pyParser.Block_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#block_stmt}.
	 * @param ctx the parse tree
	 */
	void exitBlock_stmt(@NotNull pyParser.Block_stmtContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#kparamlist}.
	 * @param ctx the parse tree
	 */
	void enterKparamlist(@NotNull pyParser.KparamlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#kparamlist}.
	 * @param ctx the parse tree
	 */
	void exitKparamlist(@NotNull pyParser.KparamlistContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#slice}.
	 * @param ctx the parse tree
	 */
	void enterSlice(@NotNull pyParser.SliceContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#slice}.
	 * @param ctx the parse tree
	 */
	void exitSlice(@NotNull pyParser.SliceContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#loop}.
	 * @param ctx the parse tree
	 */
	void enterLoop(@NotNull pyParser.LoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#loop}.
	 * @param ctx the parse tree
	 */
	void exitLoop(@NotNull pyParser.LoopContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#list_gen}.
	 * @param ctx the parse tree
	 */
	void enterList_gen(@NotNull pyParser.List_genContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#list_gen}.
	 * @param ctx the parse tree
	 */
	void exitList_gen(@NotNull pyParser.List_genContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#import_}.
	 * @param ctx the parse tree
	 */
	void enterImport_(@NotNull pyParser.Import_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#import_}.
	 * @param ctx the parse tree
	 */
	void exitImport_(@NotNull pyParser.Import_Context ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#single_stmt}.
	 * @param ctx the parse tree
	 */
	void enterSingle_stmt(@NotNull pyParser.Single_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#single_stmt}.
	 * @param ctx the parse tree
	 */
	void exitSingle_stmt(@NotNull pyParser.Single_stmtContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#dict}.
	 * @param ctx the parse tree
	 */
	void enterDict(@NotNull pyParser.DictContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#dict}.
	 * @param ctx the parse tree
	 */
	void exitDict(@NotNull pyParser.DictContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(@NotNull pyParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(@NotNull pyParser.BlockContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#assign_stmt}.
	 * @param ctx the parse tree
	 */
	void enterAssign_stmt(@NotNull pyParser.Assign_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#assign_stmt}.
	 * @param ctx the parse tree
	 */
	void exitAssign_stmt(@NotNull pyParser.Assign_stmtContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#val}.
	 * @param ctx the parse tree
	 */
	void enterVal(@NotNull pyParser.ValContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#val}.
	 * @param ctx the parse tree
	 */
	void exitVal(@NotNull pyParser.ValContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterStmts(@NotNull pyParser.StmtsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitStmts(@NotNull pyParser.StmtsContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#dict_gen}.
	 * @param ctx the parse tree
	 */
	void enterDict_gen(@NotNull pyParser.Dict_genContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#dict_gen}.
	 * @param ctx the parse tree
	 */
	void exitDict_gen(@NotNull pyParser.Dict_genContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(@NotNull pyParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(@NotNull pyParser.VarContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#module}.
	 * @param ctx the parse tree
	 */
	void enterModule(@NotNull pyParser.ModuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#module}.
	 * @param ctx the parse tree
	 */
	void exitModule(@NotNull pyParser.ModuleContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#vartuple}.
	 * @param ctx the parse tree
	 */
	void enterVartuple(@NotNull pyParser.VartupleContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#vartuple}.
	 * @param ctx the parse tree
	 */
	void exitVartuple(@NotNull pyParser.VartupleContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#op_cmp}.
	 * @param ctx the parse tree
	 */
	void enterOp_cmp(@NotNull pyParser.Op_cmpContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#op_cmp}.
	 * @param ctx the parse tree
	 */
	void exitOp_cmp(@NotNull pyParser.Op_cmpContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void enterParamlist(@NotNull pyParser.ParamlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void exitParamlist(@NotNull pyParser.ParamlistContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#simple_var}.
	 * @param ctx the parse tree
	 */
	void enterSimple_var(@NotNull pyParser.Simple_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#simple_var}.
	 * @param ctx the parse tree
	 */
	void exitSimple_var(@NotNull pyParser.Simple_varContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#elif}.
	 * @param ctx the parse tree
	 */
	void enterElif(@NotNull pyParser.ElifContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#elif}.
	 * @param ctx the parse tree
	 */
	void exitElif(@NotNull pyParser.ElifContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(@NotNull pyParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(@NotNull pyParser.ListContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#dictitem}.
	 * @param ctx the parse tree
	 */
	void enterDictitem(@NotNull pyParser.DictitemContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#dictitem}.
	 * @param ctx the parse tree
	 */
	void exitDictitem(@NotNull pyParser.DictitemContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#ifelse}.
	 * @param ctx the parse tree
	 */
	void enterIfelse(@NotNull pyParser.IfelseContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#ifelse}.
	 * @param ctx the parse tree
	 */
	void exitIfelse(@NotNull pyParser.IfelseContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#while_}.
	 * @param ctx the parse tree
	 */
	void enterWhile_(@NotNull pyParser.While_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#while_}.
	 * @param ctx the parse tree
	 */
	void exitWhile_(@NotNull pyParser.While_Context ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#karg}.
	 * @param ctx the parse tree
	 */
	void enterKarg(@NotNull pyParser.KargContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#karg}.
	 * @param ctx the parse tree
	 */
	void exitKarg(@NotNull pyParser.KargContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#except}.
	 * @param ctx the parse tree
	 */
	void enterExcept(@NotNull pyParser.ExceptContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#except}.
	 * @param ctx the parse tree
	 */
	void exitExcept(@NotNull pyParser.ExceptContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#rel_module}.
	 * @param ctx the parse tree
	 */
	void enterRel_module(@NotNull pyParser.Rel_moduleContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#rel_module}.
	 * @param ctx the parse tree
	 */
	void exitRel_module(@NotNull pyParser.Rel_moduleContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#dictlist}.
	 * @param ctx the parse tree
	 */
	void enterDictlist(@NotNull pyParser.DictlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#dictlist}.
	 * @param ctx the parse tree
	 */
	void exitDictlist(@NotNull pyParser.DictlistContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#id_list}.
	 * @param ctx the parse tree
	 */
	void enterId_list(@NotNull pyParser.Id_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#id_list}.
	 * @param ctx the parse tree
	 */
	void exitId_list(@NotNull pyParser.Id_listContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(@NotNull pyParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(@NotNull pyParser.StringContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#exprlist}.
	 * @param ctx the parse tree
	 */
	void enterExprlist(@NotNull pyParser.ExprlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#exprlist}.
	 * @param ctx the parse tree
	 */
	void exitExprlist(@NotNull pyParser.ExprlistContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#generator}.
	 * @param ctx the parse tree
	 */
	void enterGenerator(@NotNull pyParser.GeneratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#generator}.
	 * @param ctx the parse tree
	 */
	void exitGenerator(@NotNull pyParser.GeneratorContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#trycatch}.
	 * @param ctx the parse tree
	 */
	void enterTrycatch(@NotNull pyParser.TrycatchContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#trycatch}.
	 * @param ctx the parse tree
	 */
	void exitTrycatch(@NotNull pyParser.TrycatchContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#aug_op}.
	 * @param ctx the parse tree
	 */
	void enterAug_op(@NotNull pyParser.Aug_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#aug_op}.
	 * @param ctx the parse tree
	 */
	void exitAug_op(@NotNull pyParser.Aug_opContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#pos_arg}.
	 * @param ctx the parse tree
	 */
	void enterPos_arg(@NotNull pyParser.Pos_argContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#pos_arg}.
	 * @param ctx the parse tree
	 */
	void exitPos_arg(@NotNull pyParser.Pos_argContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#aug_assign}.
	 * @param ctx the parse tree
	 */
	void enterAug_assign(@NotNull pyParser.Aug_assignContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#aug_assign}.
	 * @param ctx the parse tree
	 */
	void exitAug_assign(@NotNull pyParser.Aug_assignContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#tuple}.
	 * @param ctx the parse tree
	 */
	void enterTuple(@NotNull pyParser.TupleContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#tuple}.
	 * @param ctx the parse tree
	 */
	void exitTuple(@NotNull pyParser.TupleContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#iter_gen}.
	 * @param ctx the parse tree
	 */
	void enterIter_gen(@NotNull pyParser.Iter_genContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#iter_gen}.
	 * @param ctx the parse tree
	 */
	void exitIter_gen(@NotNull pyParser.Iter_genContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#arglist}.
	 * @param ctx the parse tree
	 */
	void enterArglist(@NotNull pyParser.ArglistContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#arglist}.
	 * @param ctx the parse tree
	 */
	void exitArglist(@NotNull pyParser.ArglistContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#alias_list}.
	 * @param ctx the parse tree
	 */
	void enterAlias_list(@NotNull pyParser.Alias_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#alias_list}.
	 * @param ctx the parse tree
	 */
	void exitAlias_list(@NotNull pyParser.Alias_listContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#pos_paramlist}.
	 * @param ctx the parse tree
	 */
	void enterPos_paramlist(@NotNull pyParser.Pos_paramlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#pos_paramlist}.
	 * @param ctx the parse tree
	 */
	void exitPos_paramlist(@NotNull pyParser.Pos_paramlistContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#alias}.
	 * @param ctx the parse tree
	 */
	void enterAlias(@NotNull pyParser.AliasContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#alias}.
	 * @param ctx the parse tree
	 */
	void exitAlias(@NotNull pyParser.AliasContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(@NotNull pyParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(@NotNull pyParser.ExprContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#varlist}.
	 * @param ctx the parse tree
	 */
	void enterVarlist(@NotNull pyParser.VarlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#varlist}.
	 * @param ctx the parse tree
	 */
	void exitVarlist(@NotNull pyParser.VarlistContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#id_alias}.
	 * @param ctx the parse tree
	 */
	void enterId_alias(@NotNull pyParser.Id_aliasContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#id_alias}.
	 * @param ctx the parse tree
	 */
	void exitId_alias(@NotNull pyParser.Id_aliasContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#pos_arglist}.
	 * @param ctx the parse tree
	 */
	void enterPos_arglist(@NotNull pyParser.Pos_arglistContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#pos_arglist}.
	 * @param ctx the parse tree
	 */
	void exitPos_arglist(@NotNull pyParser.Pos_arglistContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#if_}.
	 * @param ctx the parse tree
	 */
	void enterIf_(@NotNull pyParser.If_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#if_}.
	 * @param ctx the parse tree
	 */
	void exitIf_(@NotNull pyParser.If_Context ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#set}.
	 * @param ctx the parse tree
	 */
	void enterSet(@NotNull pyParser.SetContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#set}.
	 * @param ctx the parse tree
	 */
	void exitSet(@NotNull pyParser.SetContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#class_}.
	 * @param ctx the parse tree
	 */
	void enterClass_(@NotNull pyParser.Class_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#class_}.
	 * @param ctx the parse tree
	 */
	void exitClass_(@NotNull pyParser.Class_Context ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#karglist}.
	 * @param ctx the parse tree
	 */
	void enterKarglist(@NotNull pyParser.KarglistContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#karglist}.
	 * @param ctx the parse tree
	 */
	void exitKarglist(@NotNull pyParser.KarglistContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#kparam}.
	 * @param ctx the parse tree
	 */
	void enterKparam(@NotNull pyParser.KparamContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#kparam}.
	 * @param ctx the parse tree
	 */
	void exitKparam(@NotNull pyParser.KparamContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(@NotNull pyParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(@NotNull pyParser.ProgContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#with}.
	 * @param ctx the parse tree
	 */
	void enterWith(@NotNull pyParser.WithContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#with}.
	 * @param ctx the parse tree
	 */
	void exitWith(@NotNull pyParser.WithContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#func}.
	 * @param ctx the parse tree
	 */
	void enterFunc(@NotNull pyParser.FuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#func}.
	 * @param ctx the parse tree
	 */
	void exitFunc(@NotNull pyParser.FuncContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#block_head}.
	 * @param ctx the parse tree
	 */
	void enterBlock_head(@NotNull pyParser.Block_headContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#block_head}.
	 * @param ctx the parse tree
	 */
	void exitBlock_head(@NotNull pyParser.Block_headContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(@NotNull pyParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(@NotNull pyParser.StmtContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#mod_list}.
	 * @param ctx the parse tree
	 */
	void enterMod_list(@NotNull pyParser.Mod_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#mod_list}.
	 * @param ctx the parse tree
	 */
	void exitMod_list(@NotNull pyParser.Mod_listContext ctx);

	/**
	 * Enter a parse tree produced by {@link pyParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(@NotNull pyParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(@NotNull pyParser.AssignContext ctx);
}
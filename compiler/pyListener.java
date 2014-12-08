// Generated from py.g4 by ANTLR 4.4
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link pyParser}.
 */
public interface pyListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link pyParser#tuple_}.
	 * @param ctx the parse tree
	 */
	void enterTuple_(@NotNull pyParser.Tuple_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#tuple_}.
	 * @param ctx the parse tree
	 */
	void exitTuple_(@NotNull pyParser.Tuple_Context ctx);
	/**
	 * Enter a parse tree produced by the {@code assert_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterAssert_stmt(@NotNull pyParser.Assert_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assert_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitAssert_stmt(@NotNull pyParser.Assert_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link pyParser#set_}.
	 * @param ctx the parse tree
	 */
	void enterSet_(@NotNull pyParser.Set_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#set_}.
	 * @param ctx the parse tree
	 */
	void exitSet_(@NotNull pyParser.Set_Context ctx);
	/**
	 * Enter a parse tree produced by the {@code index__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIndex__is__expr(@NotNull pyParser.Index__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code index__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIndex__is__expr(@NotNull pyParser.Index__is__exprContext ctx);
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
	 * Enter a parse tree produced by the {@code raise_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterRaise_stmt(@NotNull pyParser.Raise_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code raise_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitRaise_stmt(@NotNull pyParser.Raise_stmtContext ctx);
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
	 * Enter a parse tree produced by the {@code funccall__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFunccall__is__expr(@NotNull pyParser.Funccall__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code funccall__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFunccall__is__expr(@NotNull pyParser.Funccall__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code func_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterFunc_stmt(@NotNull pyParser.Func_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code func_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitFunc_stmt(@NotNull pyParser.Func_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link pyParser#elif_}.
	 * @param ctx the parse tree
	 */
	void enterElif_(@NotNull pyParser.Elif_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#elif_}.
	 * @param ctx the parse tree
	 */
	void exitElif_(@NotNull pyParser.Elif_Context ctx);
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
	 * Enter a parse tree produced by the {@code bit_and__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBit_and__is__expr(@NotNull pyParser.Bit_and__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code bit_and__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBit_and__is__expr(@NotNull pyParser.Bit_and__is__exprContext ctx);
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
	 * Enter a parse tree produced by {@link pyParser#str_prefix}.
	 * @param ctx the parse tree
	 */
	void enterStr_prefix(@NotNull pyParser.Str_prefixContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#str_prefix}.
	 * @param ctx the parse tree
	 */
	void exitStr_prefix(@NotNull pyParser.Str_prefixContext ctx);
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
	 * Enter a parse tree produced by the {@code ternary__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterTernary__is__expr(@NotNull pyParser.Ternary__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ternary__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitTernary__is__expr(@NotNull pyParser.Ternary__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code global_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterGlobal_stmt(@NotNull pyParser.Global_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code global_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitGlobal_stmt(@NotNull pyParser.Global_stmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code and__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAnd__is__expr(@NotNull pyParser.And__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code and__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAnd__is__expr(@NotNull pyParser.And__is__exprContext ctx);
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
	 * Enter a parse tree produced by {@link pyParser#blockend}.
	 * @param ctx the parse tree
	 */
	void enterBlockend(@NotNull pyParser.BlockendContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#blockend}.
	 * @param ctx the parse tree
	 */
	void exitBlockend(@NotNull pyParser.BlockendContext ctx);
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
	 * Enter a parse tree produced by the {@code or__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOr__is__expr(@NotNull pyParser.Or__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code or__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOr__is__expr(@NotNull pyParser.Or__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code dash_calc__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDash_calc__is__expr(@NotNull pyParser.Dash_calc__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code dash_calc__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDash_calc__is__expr(@NotNull pyParser.Dash_calc__is__exprContext ctx);
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
	 * Enter a parse tree produced by {@link pyParser#except_}.
	 * @param ctx the parse tree
	 */
	void enterExcept_(@NotNull pyParser.Except_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#except_}.
	 * @param ctx the parse tree
	 */
	void exitExcept_(@NotNull pyParser.Except_Context ctx);
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
	 * Enter a parse tree produced by the {@code brackets__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBrackets__is__expr(@NotNull pyParser.Brackets__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code brackets__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBrackets__is__expr(@NotNull pyParser.Brackets__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code print_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterPrint_stmt(@NotNull pyParser.Print_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code print_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitPrint_stmt(@NotNull pyParser.Print_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link pyParser#int_}.
	 * @param ctx the parse tree
	 */
	void enterInt_(@NotNull pyParser.Int_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#int_}.
	 * @param ctx the parse tree
	 */
	void exitInt_(@NotNull pyParser.Int_Context ctx);
	/**
	 * Enter a parse tree produced by the {@code loop_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterLoop_stmt(@NotNull pyParser.Loop_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code loop_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitLoop_stmt(@NotNull pyParser.Loop_stmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code pass_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterPass_stmt(@NotNull pyParser.Pass_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code pass_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitPass_stmt(@NotNull pyParser.Pass_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link pyParser#slice_}.
	 * @param ctx the parse tree
	 */
	void enterSlice_(@NotNull pyParser.Slice_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#slice_}.
	 * @param ctx the parse tree
	 */
	void exitSlice_(@NotNull pyParser.Slice_Context ctx);
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
	 * Enter a parse tree produced by the {@code exec_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterExec_stmt(@NotNull pyParser.Exec_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code exec_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitExec_stmt(@NotNull pyParser.Exec_stmtContext ctx);
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
	 * Enter a parse tree produced by the {@code not__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNot__is__expr(@NotNull pyParser.Not__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code not__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNot__is__expr(@NotNull pyParser.Not__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code bit_xor__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBit_xor__is__expr(@NotNull pyParser.Bit_xor__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code bit_xor__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBit_xor__is__expr(@NotNull pyParser.Bit_xor__is__exprContext ctx);
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
	 * Enter a parse tree produced by the {@code lambda_label__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLambda_label__is__expr(@NotNull pyParser.Lambda_label__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lambda_label__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLambda_label__is__expr(@NotNull pyParser.Lambda_label__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link pyParser#list_}.
	 * @param ctx the parse tree
	 */
	void enterList_(@NotNull pyParser.List_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#list_}.
	 * @param ctx the parse tree
	 */
	void exitList_(@NotNull pyParser.List_Context ctx);
	/**
	 * Enter a parse tree produced by the {@code attr__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAttr__is__expr(@NotNull pyParser.Attr__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code attr__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAttr__is__expr(@NotNull pyParser.Attr__is__exprContext ctx);
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
	 * Enter a parse tree produced by {@link pyParser#id_}.
	 * @param ctx the parse tree
	 */
	void enterId_(@NotNull pyParser.Id_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#id_}.
	 * @param ctx the parse tree
	 */
	void exitId_(@NotNull pyParser.Id_Context ctx);
	/**
	 * Enter a parse tree produced by {@link pyParser#set_gen}.
	 * @param ctx the parse tree
	 */
	void enterSet_gen(@NotNull pyParser.Set_genContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#set_gen}.
	 * @param ctx the parse tree
	 */
	void exitSet_gen(@NotNull pyParser.Set_genContext ctx);
	/**
	 * Enter a parse tree produced by the {@code shift__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterShift__is__expr(@NotNull pyParser.Shift__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code shift__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitShift__is__expr(@NotNull pyParser.Shift__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code exponentiation__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExponentiation__is__expr(@NotNull pyParser.Exponentiation__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code exponentiation__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExponentiation__is__expr(@NotNull pyParser.Exponentiation__is__exprContext ctx);
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
	 * Enter a parse tree produced by the {@code import_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterImport_stmt(@NotNull pyParser.Import_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code import_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitImport_stmt(@NotNull pyParser.Import_stmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unary__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnary__is__expr(@NotNull pyParser.Unary__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unary__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnary__is__expr(@NotNull pyParser.Unary__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link pyParser#lambda_}.
	 * @param ctx the parse tree
	 */
	void enterLambda_(@NotNull pyParser.Lambda_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#lambda_}.
	 * @param ctx the parse tree
	 */
	void exitLambda_(@NotNull pyParser.Lambda_Context ctx);
	/**
	 * Enter a parse tree produced by the {@code bit_or__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBit_or__is__expr(@NotNull pyParser.Bit_or__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code bit_or__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBit_or__is__expr(@NotNull pyParser.Bit_or__is__exprContext ctx);
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
	 * Enter a parse tree produced by {@link pyParser#float_}.
	 * @param ctx the parse tree
	 */
	void enterFloat_(@NotNull pyParser.Float_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#float_}.
	 * @param ctx the parse tree
	 */
	void exitFloat_(@NotNull pyParser.Float_Context ctx);
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
	 * Enter a parse tree produced by the {@code dot_calc__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDot_calc__is__expr(@NotNull pyParser.Dot_calc__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code dot_calc__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDot_calc__is__expr(@NotNull pyParser.Dot_calc__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link pyParser#str_val}.
	 * @param ctx the parse tree
	 */
	void enterStr_val(@NotNull pyParser.Str_valContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#str_val}.
	 * @param ctx the parse tree
	 */
	void exitStr_val(@NotNull pyParser.Str_valContext ctx);
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
	 * Enter a parse tree produced by the {@code val_label__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVal_label__is__expr(@NotNull pyParser.Val_label__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code val_label__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVal_label__is__expr(@NotNull pyParser.Val_label__is__exprContext ctx);
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
	 * Enter a parse tree produced by the {@code comparison__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterComparison__is__expr(@NotNull pyParser.Comparison__is__exprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comparison__is__expr}
	 * labeled alternative in {@link pyParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitComparison__is__expr(@NotNull pyParser.Comparison__is__exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link pyParser#dict_}.
	 * @param ctx the parse tree
	 */
	void enterDict_(@NotNull pyParser.Dict_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#dict_}.
	 * @param ctx the parse tree
	 */
	void exitDict_(@NotNull pyParser.Dict_Context ctx);
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
	 * Enter a parse tree produced by {@link pyParser#with_}.
	 * @param ctx the parse tree
	 */
	void enterWith_(@NotNull pyParser.With_Context ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#with_}.
	 * @param ctx the parse tree
	 */
	void exitWith_(@NotNull pyParser.With_Context ctx);
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
	 * Enter a parse tree produced by {@link pyParser#blockbegin}.
	 * @param ctx the parse tree
	 */
	void enterBlockbegin(@NotNull pyParser.BlockbeginContext ctx);
	/**
	 * Exit a parse tree produced by {@link pyParser#blockbegin}.
	 * @param ctx the parse tree
	 */
	void exitBlockbegin(@NotNull pyParser.BlockbeginContext ctx);
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
	 * Enter a parse tree produced by the {@code del_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void enterDel_stmt(@NotNull pyParser.Del_stmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code del_stmt}
	 * labeled alternative in {@link pyParser#stmts}.
	 * @param ctx the parse tree
	 */
	void exitDel_stmt(@NotNull pyParser.Del_stmtContext ctx);
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
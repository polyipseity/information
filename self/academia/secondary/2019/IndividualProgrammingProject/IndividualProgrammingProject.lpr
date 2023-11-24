program IndividualProgrammingProject;

{$mode objfpc}{$H+}{$A4}

uses
  {$IFDEF UNIX}{$IFDEF UseCThreads}
  cthreads,
  {$ENDIF}{$ENDIF}
  //cmem,
  {$IFDEF useHeapTrace}
  heaptrc,
  {$ENDIF}
  Interfaces, // this includes the LCL widgetset
  Forms, LazOpenGLContext,
  UnitFormMain;

{$R *.res}

begin
  {$IFDEF useHeapTrace}
  //globalSkipIfNoLeaks:=true;
  {$ENDIF}
  Randomize;
  RequireDerivedFormResource:=true;
  Application.Scaled:=True; // Lazarus cannot recognize with Application do.
  with Application do
  begin
    //Scaled:=true;
    Initialize;
    CreateForm(TFormMain, FormMain);
    Run;
  end;
end.


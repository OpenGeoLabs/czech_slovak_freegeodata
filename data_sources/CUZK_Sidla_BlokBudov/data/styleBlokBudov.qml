<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingTol="1" readOnly="0" minScale="200000" simplifyMaxScale="1" simplifyDrawingHints="1" simplifyLocal="1" labelsEnabled="0" simplifyAlgorithm="0" version="3.8.3-Zanzibar" hasScaleBasedVisibilityFlag="1" styleCategories="AllStyleCategories" maxScale="100">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" symbollevels="0" forceraster="0" enableorderby="0">
    <symbols>
      <symbol type="fill" clip_to_extent="1" alpha="1" force_rhr="0" name="0">
        <layer pass="0" enabled="1" locked="0" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="176,170,160,255"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="78,78,78,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_unit" v="Point"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions" value="JMENO"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory height="15" opacity="1" maxScaleDenominator="1e+08" width="15" lineSizeScale="3x:0,0,0,0,0,0" enabled="0" penAlpha="255" backgroundColor="#ffffff" sizeScale="3x:0,0,0,0,0,0" lineSizeType="MM" penColor="#000000" penWidth="0" rotationOffset="270" diagramOrientation="Up" barWidth="5" minScaleDenominator="100" minimumSize="0" labelPlacementMethod="XHeight" backgroundAlpha="255" scaleDependency="Area" sizeType="MM" scaleBasedVisibility="0">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute color="#000000" field="" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" dist="0" zIndex="0" placement="1" showAll="1" linePlacementFlags="18" obstacle="0">
    <properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option type="double" value="0" name="allowedGapsBuffer"/>
        <Option type="bool" value="false" name="allowedGapsEnabled"/>
        <Option type="QString" value="" name="allowedGapsLayer"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <fieldConfiguration/>
  <aliases/>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults/>
  <constraints/>
  <constraintExpressions/>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column type="actions" width="-1" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="DATA50_K"/>
    <field editable="1" name="DATA50_P"/>
    <field editable="1" name="JMENO"/>
    <field editable="1" name="SHAPE_Area"/>
    <field editable="1" name="SHAPE_Leng"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="DATA50_K"/>
    <field labelOnTop="0" name="DATA50_P"/>
    <field labelOnTop="0" name="JMENO"/>
    <field labelOnTop="0" name="SHAPE_Area"/>
    <field labelOnTop="0" name="SHAPE_Leng"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>JMENO</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
